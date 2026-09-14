from django.test import TestCase

from django.urls import reverse 

from .models import Publisher, Book 

class BookListTest(TestCase):
    def test_books_page_shows_The_pale_writer(self):
        publisher = Publisher.objects.create(name="Righter Ofalot")
        Book.objects.create(publisher=publisher, title="The Pale Writer")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Pale Writer")