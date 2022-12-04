from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from user.models import Account

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)


    def __str__(self):
        return self.slug

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
    name = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, related_name='+')
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True, blank=True)
    nickname = models.CharField(max_length=50, default='', null=True)

    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL)
    star_point = models.ForeignKey(Star, null=True, blank=False, on_delete=models.SET_NULL)  # 별점
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}:{self.title}'

class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.FileField(upload_to="review") # media/review/에 저장

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, related_name='+')
    nickname = models.CharField(max_length=50, default='', null=True)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} commented {self.post} post : {self.content} comment'

class User(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    userid = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.userid