from django.test import TestCase
from MelkaJewellery.accounts.models import AppAccount, Profile


class ProfileModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = AppAccount.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
        )

    def test_profile_creation(self):

        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.first_name, None)  # Default value
        self.assertEqual(profile.last_name, None)  # Default value
        self.assertEqual(profile.age, None)  # Default value
        self.assertIsNone(profile.image)  # CloudinaryField default value

    def test_str_representation_with_name(self):

        profile = Profile.objects.get(user=self.user)
        profile.first_name = "John"
        profile.last_name = "Doe"
        profile.save()
        self.assertEqual(str(profile), "John Doe")

    def test_cloudinary_field(self):

        profile = Profile.objects.get(user=self.user)
        profile.image = "test_image.jpg"
        profile.save()
        self.assertEqual(profile.image, "test_image.jpg")

    def test_update_profile_fields(self):

        profile = Profile.objects.get(user=self.user)
        profile.first_name = "Jane"
        profile.last_name = "Doe"
        profile.age = 30
        profile.image = "updated_image.jpg"
        profile.save()

        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.first_name, "Jane")
        self.assertEqual(updated_profile.last_name, "Doe")
        self.assertEqual(updated_profile.age, 30)


class AppAccountModelTests(TestCase):
    def test_create_user(self):

        user = AppAccount.objects.create_user(
            username="newuser",
            email="newuser@example.com",
            password="securepassword",
        )
        self.assertEqual(user.username, "newuser")
        self.assertEqual(user.email, "newuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        superuser = AppAccount.objects.create_superuser(
            username="adminuser",
            email="adminuser@example.com",
            password="securepassword",
        )
        self.assertEqual(superuser.username, "adminuser")
        self.assertEqual(superuser.email, "adminuser@example.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_str_representation(self):
       
        user = AppAccount.objects.create_user(
            username="strtestuser",
            email="strtestuser@example.com",
            password="password123",
        )
        self.assertEqual(str(user), "strtestuser")
