from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

class UserLoginAPIViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.url = reverse('user_login')

    def test_login_with_valid_credentials(self):
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertTrue('token' in response.data)

    def test_login_with_invalid_credentials(self):
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
class UserRegisterAPIViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('user_register')

    def test_register_with_valid_data(self):
        data = {
            'username': 'testuser', 
            'first_name': 'testfirst', 
            'last_name': 'testlast', 
            'email': 'test@test.com', 
            'password': 'testpass', 
            'password2': 'testpass'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_register_with_mismatched_passwords(self):
        data = {
            'username': 'testuser', 
            'first_name': 'testfirst', 
            'last_name': 'testlast', 
            'email': 'test@test.com', 
            'password': 'testpass', 
            'password2': 'wrongpass'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_register_with_existing_username(self):
        User.objects.create_user(username='testuser', password='testpass')
        data = {
            'username': 'testuser', 
            'first_name': 'testfirst', 
            'last_name': 'testlast', 
            'email': 'test@test.com', 
            'password': 'testpass', 
            'password2': 'testpass'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        
        
class UserLogoutAPIViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.url = reverse('user_logout')

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(key=self.token.key).exists())

    def test_logout_without_token(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)