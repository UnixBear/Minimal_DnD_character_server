from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
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
        # self.assertEqual(self.post.get_absolute_url(),"/{}/character/{}".format(str(self.post), str(self.post.pk))")
        # print(self.post.get_absolute_url())

    def test_url_exists_at_correct_location(self):
        response = self.client.get(
            f"/{self.post.author}/character/{self.post.pk}", follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get(
            f"/{self.post.author}/character/{self.post.pk}", follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_character_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Wizard")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(
            reverse("character_details", args=[self.post.author, self.post.pk]),
            follow=True,
        )
        no_response = self.client.get(
            "/{}/character/100".format(str(self.post)), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "testbold")
        self.assertTemplateUsed(response, "character_details.html")
