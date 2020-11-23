"""
    Like views but with classes
"""
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from posts.forms import PostForm


class IndexView(ListView):
    template_name = 'post/index.html'
    model = Post # this view is related to model Post

    # # 1st method send only 1 element to front-end
    # queryset = Post.objects.all()
    # context_object_name = 'posts' # element that you send inside context

    # 2nd method send any number of elements
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['form'] = PostForm()
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'image', 'status', 'author']
    http_method_names = ['post']
    success_url = ''
    login_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/details.html'
    pk_url_kwarg = 'id' # use id in url address
    login_url = '/login'


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/edit.html'
    pk_url_kwarg = 'id'
    login_url = '/login'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post/delete_confirm.html'
    success_url = '/'
    login_url = '/login'
