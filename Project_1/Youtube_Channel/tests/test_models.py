from rest_framework.test import APITestCase
from CryceTruly.models import User

extra_fields = {
        'is_staff': True,
        'is_superuser': True
    }

class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('Anil', 'anil@example.com', 'Password@123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'anil@example.com')
        self.assertFalse(user.is_staff, False)

    def test_create_super_user(self):
        user = User.objects.create_superuser('Anil', 'anil@example.com', 'Password@123')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'anil@example.com')
        self.assertTrue(user.is_staff)

    def test_create_super_user_is_staff_status_check(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username="", email='anil@example.com', password='Password@123', is_staff=False)

    def test_create_super_user_is_superuser_status_check(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username="", email='anil@example.com', password='Password@123', is_superuser=False)

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='anil@example.com', password='Password@123')

    def test_raises_with_error_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Users must have an username'):
            User.objects.create_user(username="", email='anil@example.com', password='Password@123')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="Anil",email='', password='Password@123')


    def test_raises_with_error_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Users must have an email address'):
            User.objects.create_user(username="Anil", email='', password='Password@123')
