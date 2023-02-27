from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import charSheet


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = charSheet.objects.create(
            char_name="testbold",
            character_class="Wizard",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.char_name, "testbold")
        self.assertEqual(self.post.character_class, "Wizard")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.initiative, 0)
        self.assertEqual(str(self.post), "testbold")
        self.assertEqual(self.post.pk, 1)
        print(self.post.get_absolute_url())

    def test_url_exists_at_correct_location(self):
        response = self.client.get(
            "/{}/character/{}".format(str(self.post), str(self.post.pk))
        )
        self.assertEqual(response.status_code, 200)
