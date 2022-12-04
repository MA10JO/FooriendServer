from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from user.models import Account


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
    name = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, related_name='+')
    nickname = models.CharField(max_length=50, default='', null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True, blank=True)
    party = models.CharField(max_length=30)

    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, blank=False, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}:{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True, related_name='+')
    nickname = models.CharField(max_length=50, default='', null=True)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} commented {self.post} post : {self.content} comment'