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
        return f'/review/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Star(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/review/star/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Star'


class Post(models.Model):
    #음식점 이름
    title = models.CharField(max_length=30)

    #장소=지역
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL)

    head_image = models.ImageField(upload_to='review/images/%Y/%m/%d/', blank=True)
    #%Y 2022, %y 22
    star_point = models.ForeignKey(Star, null=True, blank=False, on_delete=models.SET_NULL)  #별점

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 추후 author 작성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author} : {self.created_at}'

    def get_absolute_url(self):
        return f'/review/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] # a.txt => a txt


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'