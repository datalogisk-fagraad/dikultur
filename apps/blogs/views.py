from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    View

from django.utils import timezone

from . import models, forms

class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    queryset = models.Blog.objects.order_by('title')


class BlogDetail(DetailView):
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'
    model = models.Blog


class PostCreate(CreateView):
    template_name = 'blogs/post_form.html'
    model = models.Post
    form_class = forms.PostForm

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get('slug', None)
        self.blog = models.Blog.objects.get(slug=slug)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if not user in self.blog.owners.all():
            return HttpResponse('Access denied')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.blog = self.blog
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['blog'] = self.blog
        return kwargs


class PostDetail(DetailView):
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'
    model = models.Post

class PostUpdate(UpdateView):
    template_name = 'blogs/post_form.html'
    model = models.Post
    form_class = forms.PostForm

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get('blog_slug', None)
        self.blog = models.Blog.objects.get(slug=slug)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if not user in self.blog.owners.all():
            return HttpResponse('Access denied')
        return super().get(request, *args, **kwargs)

class BlogIndex(ListView):
    template_name = 'blogs/blog_index.html'
    context_object_name = 'posts'

    def dispatch(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug', None)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = models.Post.objects.public().order_by('created_at')
        return queryset
