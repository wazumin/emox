from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from .views import *

# Create your tests here.

class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")

class CreateCommentTest(TestCase):
    def test_should_resolve_comment_new(self):
        found = resolve("/comments/new/")
        self.assertEqual(comment_new, found.func)
