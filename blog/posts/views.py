from django.shortcuts import render, redirect
from django.http import HttpResponse
# decorator that checks a user for authorization
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.forms import PostForm

# every controller must have 1 argument and return HttpResponse

def index(request):
    # getting all posts from DB
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'form': PostForm()
    }
    return render(request, 'post/index.html', context) # from templates directory


@login_required(login_url='/login')
def detail(request, id):
    # return HttpResponse(f'<h1>Blog post #{id}</h1>')
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'post/details.html', context)

# for creating posts in main page
@login_required(login_url='/login')
def create_post(request):
    form = PostForm(request.POST, request.FILES)
    # validating all fields
    if form.is_valid():
        form.save()
    return redirect('main')


@login_required(login_url='/login')
def edit_post(request, id):
    if request.method == 'GET':
        # send edit page to user
        post = Post.objects.get(pk=id)
        form = PostForm(instance=post)
        return render(request, 'post/edit.html', { 'form': form, 'post': post })
    else:
        # validate and save edited post
        post = Post.objects.get(id=id)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('main')


@login_required(login_url='/login')
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('main')
