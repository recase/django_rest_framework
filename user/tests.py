from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="test@test.com", password="12345", first_name="test", last_name="user")
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'user')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(str(user), 'test@test.com')

        try:
            self.assertIsNone(user.usernme)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="password")

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email="test@test.com", password="password", first_name="test", last_name="user")
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'user')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_superuser()
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email='')
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="test@test.com", password='password', is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="test@test.com", password="password", is_staff=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="test@test.com", password='password', is_active=False)
