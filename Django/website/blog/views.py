from django.shortcuts import render, get_object_or_404

# Create your views here.

from blog.models import  Post

def allpost(request):
    posts = Post.objects.all();
    print(posts)
    return render(request, 'posts.html', {'posts': posts})

def detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'details.html', {'detail': detail})