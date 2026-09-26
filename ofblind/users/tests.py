from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(TestCase):

    # тест вызова страницы регистрации
    def test_registration_page_status_code(self):
        url = reverse('users:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    # тест регистрации успешной авторизации пользователя и выхода
    def test_successful_user_auth(self):
        url = reverse('users:signup')
        form_data = {
            'username': 'newtestuser',
            'email': 'newtestemail@mail.com',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!', 
        }
        
        response = self.client.post(url, data=form_data)
        
        self.assertEqual(response.status_code, 302)
        
        user_exists = User.objects.filter(username='newtestuser').exists()
        self.assertTrue(user_exists)

        url = reverse('users:signin')
        form_data = {
            'username': 'newtestuser',
            'password': 'StrongPassword123!',
        }

        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

        url = reverse('users:logout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)