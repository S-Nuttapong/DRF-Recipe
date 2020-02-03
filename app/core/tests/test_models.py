from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'Jwebb@gmail.com'
        password = 'sun123312'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a newe user is normalized"""
        email = 'jwebb@Gmail.com'
        user = get_user_model().objects.create_user(email, 'sun123321')

        self.assertEqual(user.email, email.lower()) #string method for lower case
    
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        #test if we've implemented validate function in case users create account without email
        with self.assertRaises(ValueError): #use assert -> Raise
            get_user_model().objects.create_user(None, 'sun123321')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'jwebb@Gmail.com',
            'sun123321'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)