from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthenticationTests(TestCase):

    # тест вызова страницы регистрации
    def test_registration_page_status_code(self):
        url = reverse('users:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    # тест регистрации успешной регистрации пользователя
    def test_successful_user_registration(self):
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
