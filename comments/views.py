from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
# Create your views here.

def top(request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, "comments/top.html", context)

def comment_new(request):
    return HttpResponse('コメントの登録')

def comment_edit(request, comment_id):
    return HttpResponse('コメントの編集')

def comment_detail(request, comment_id):
    return HttpResponse('コメントの詳細')