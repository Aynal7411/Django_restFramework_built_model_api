from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from snippets.models import Snippet


class SnippetApiTests(APITestCase):
    def setUp(self):
        self.snippet = Snippet.objects.create(
            title="Hello world",
            code='print("hello world")',
            linenos=True,
            language="python",
            style="friendly",
        )

    def test_list_snippets(self):
        url = reverse("snippet-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["id"], self.snippet.id)

    def test_retrieve_snippet(self):
        url = reverse("snippet-detail", args=[self.snippet.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["code"], self.snippet.code)

    def test_create_snippet(self):
        url = reverse("snippet-list")
        payload = {
            "title": "New snippet",
            "code": 'print("new snippet")',
            "linenos": False,
            "language": "python",
            "style": "friendly",
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], payload["title"])
        self.assertEqual(Snippet.objects.count(), 2)

    def test_update_snippet(self):
        url = reverse("snippet-detail", args=[self.snippet.pk])
        payload = {
            "title": "Updated title",
            "code": self.snippet.code,
            "linenos": self.snippet.linenos,
            "language": self.snippet.language,
            "style": self.snippet.style,
        }

        response = self.client.put(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.snippet.refresh_from_db()
        self.assertEqual(self.snippet.title, "Updated title")

    def test_partial_update_snippet(self):
        url = reverse("snippet-detail", args=[self.snippet.pk])
        payload = {"title": "Partially updated"}

        response = self.client.patch(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.snippet.refresh_from_db()
        self.assertEqual(self.snippet.title, "Partially updated")

    def test_delete_snippet(self):
        url = reverse("snippet-detail", args=[self.snippet.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippet.objects.count(), 0)

