from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
# every controller must have 1 argument and return HttpResponse
def index(request):
    # getting all posts from DB
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/index.html', context) # from templates directory

def detail(request, id):
    # return HttpResponse(f'<h1>Blog post #{id}</h1>')
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'post/details.html', context)
