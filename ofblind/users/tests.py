from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()

class UserActivationTests(TestCase):

    def setUp(self):
        self.register_url = reverse('users:signup')
        self.login_url = reverse('users:signin')
        self.logout_url = reverse('users:logout')
        
        self.form_data = {
            'username': 'newtestuser',
            'email': 'newtestemail@mail.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!', 
        }

    def test_registration_page_status_code(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_successful_registration_sends_email(self):
        response = self.client.post(self.register_url, data=self.form_data)
        
        self.assertEqual(response.status_code, 302)
        
        user = User.objects.get(username='newtestuser')
        self.assertFalse(user.is_active)
        
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Активация вашего аккаунта', mail.outbox[0].subject)
        self.assertEqual(mail.outbox[0].to, ['newtestemail@mail.com'])

    def test_successful_activation(self):

        self.client.post(self.register_url, data=self.form_data)
        user = User.objects.get(username='newtestuser')
        
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        
        activation_url = reverse('users:activate', kwargs={'uidb64': uidb64, 'token': token})
        response = self.client.get(activation_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/activation_success.html')
        
        user.refresh_from_db()
        self.assertTrue(user.is_active)

    def test_auth_flow_inactive_and_active(self):
        self.client.post(self.register_url, data=self.form_data)
        
        login_data = {'username': 'newtestuser', 'password': 'StrongPassword123!'}
        response = self.client.post(self.login_url, data=login_data)
        
        self.assertNotIn('_auth_user_id', self.client.session)

        user = User.objects.get(username='newtestuser')
        user.is_active = True
        user.save()

        response = self.client.post(self.login_url, data=login_data)
        
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)
