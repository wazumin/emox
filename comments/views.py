from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def top(request):
    return HttpResponse("Hello World")

def comment_new(request):
    return HttpResponse('コメントの登録')

def comment_edit(request, comment_id):
    return HttpResponse('コメントの編集')

def comment_detail(request, comment_id):
    return HttpResponse('コメントの詳細')