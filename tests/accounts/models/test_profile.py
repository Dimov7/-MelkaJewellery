from django.test import TestCase
from django.contrib.auth import get_user_model

from MelkaJewellery.accounts.models.profile import Profile

UserModel = get_user_model()


class ProfileModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

    def test_create_profile_with_all_fields(self):
        # Create a profile with all fields populated
        profile = Profile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            age=30,
            image='test_image_url'
        )

        # Assertions
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.first_name, 'John')
        self.assertEqual(profile.last_name, 'Doe')
        self.assertEqual(profile.age, 30)
        self.assertEqual(profile.image, 'test_image_url')
        self.assertEqual(str(profile), 'John Doe')

    def test_create_profile_with_partial_fields(self):
        # Create a profile with only some fields populated
        profile = Profile.objects.create(
            user=self.user,
            first_name='Jane',
            age=25,
        )

        # Assertions
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.first_name, 'Jane')
        self.assertEqual(profile.last_name, None)  # Default null
        self.assertEqual(profile.age, 25)
        self.assertEqual(profile.image, None)  # Default null
        self.assertEqual(str(profile), 'Jane')

    def test_create_profile_without_optional_fields(self):
        # Create a profile without optional fields
        profile = Profile.objects.create(
            user=self.user
        )

        # Assertions
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.first_name, None)  # Default null
        self.assertEqual(profile.last_name, None)  # Default null
        self.assertEqual(profile.age, None)  # Default null
        self.assertEqual(profile.image, None)  # Default null
        self.assertEqual(str(profile), '')  # No name provided

    def test_profile_str_representation(self):
        # Test string representation when both names are provided
        profile = Profile.objects.create(
            user=self.user,
            first_name='Alice',
            last_name='Smith'
        )
        self.assertEqual(str(profile), 'Alice Smith')

        # Test string representation with only first name
        profile = Profile.objects.create(
            user=self.user,
            first_name='Alice'
        )
        self.assertEqual(str(profile), 'Alice')

        # Test string representation with no names
        profile = Profile.objects.create(
            user=self.user
        )
        self.assertEqual(str(profile), '')

    def test_profile_is_linked_to_user(self):
        # Ensure that the Profile is linked to the correct User
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.user.username, 'testuser')

    def test_profile_age_validation(self):
        # Ensure invalid ages cannot be set (negative numbers)
        with self.assertRaises(ValueError):
            Profile.objects.create(
                user=self.user,
                age=-5
            )
