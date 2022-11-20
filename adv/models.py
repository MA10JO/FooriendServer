from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/adv/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class State(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/adv/state/{self.slug}/'

    class Meta:
        verbose_name_plural = 'State'


class Post(models.Model):
    #모집 완료 or 모집 중
    state = models.ForeignKey(State, null=True, blank=False, on_delete=models.SET_NULL)

    #음식점 이름
    title = models.CharField(max_length=30)
    #장소=지역
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL)

    #모집 인원
    party = models.CharField(max_length=30)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 추후 author 작성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')


    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author} : {self.created_at}'

    def get_absolute_url(self):
        return f'/adv/{self.pk}/'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'