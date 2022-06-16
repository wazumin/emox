from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory
from django.urls import resolve
from .views import *
from .models import Comment

UserModel = get_user_model()

# Create your tests here.

class TopPageRenderCommentsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.comment = Comment.objects.create(
            emotion="emotion1",
            description="description1",
            created_by=self.user
        )
        
    def test_should_return_comment_emotion(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.comment.emotion)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)
    
    # def test_should_return_description(self):
    #     request = RequestFactory().get("/")
    #     request.user = self.user
    #     response = top(request)
    #     self.assertNotContains(response, self.comment.description)

class CreateCommentTest(TestCase):
    def test_should_resolve_comment_new(self):
        found = resolve("/comments/new/")
        self.assertEqual(comment_new, found.func)

class CommentDetailTest(TestCase):
    def test_should_resolve_comment_detail(self):
        found = resolve("/comments/1/")
        self.assertEqual(comment_detail, found.func)

class EditCommentTest(TestCase):
    def test_should_resolve_comment_edit(self):
        found = resolve("/comments/1/edit/")
        self.assertEqual(comment_edit, found.func)

class TopPageViewTest(TestCase):
    def test_top_page_returns_200_and_expected_emotion(self):
        response = self.client.get('/')
        self.assertContains(response, "Emox_App", status_code=200)
    
    def test_top_page_uses_expected_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "comments/top.html")