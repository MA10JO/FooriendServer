from django.shortcuts import render, redirect
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

# Create your views here.
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            return response
        else:
            return redirect('/community/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate,self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
    # 템플릿은 모델명_list.html : post_list.html
    # 매개변수 모델명_list : post_list

class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델명_detail.html : post_detail.html
    # 매개변수 모델명 : post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

def category_page(request, slug):
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
        return render(request, 'community/post_list.html', {
            'category' : category,
            'post_list' : post_list,
            'categories' : Category.objects.all()
        })