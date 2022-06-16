from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.

def top(request):
    comments = Comment.objects.all()
    context = {"comments": comments}
    return render(request, "comments/top.html", context)

@login_required
def comment_new(request):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.save()
            return redirect(comment_detail, comment_id=comment.pk)
    else:
        form = CommentForm()
    return render(request, "comments/comment_new.html", {'form': form})

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.created_by_id != request.user.id:
        return HttpResponseForbidden("このコメントの編集は許可されていません")
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_detail', comment_id=comment_id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'comments/comment_edit.html', {'form', form})

def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, "comments/comment_detail.html", {'comment': comment})