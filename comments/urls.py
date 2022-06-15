from django.urls import path
from .views import *

urlpatterns = [
    path('new/', comment_new, name="comment_new"),
    path('<int_comment_id>/', comment_detail, name="comment_detail"),
    path('<int_comment_id>/edit/', comment_edit, name="comment_edit"),
]