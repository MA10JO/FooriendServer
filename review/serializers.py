from rest_framework import serializers
from .models import *

class UserSerializser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['post', 'userid']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['post', 'content']

class CommentSerializer(serializers.ModelSerializer):
    author_userid = UserSerializser(read_only=True)
    class Meta:
        model = Comment
        fields = ['post', 'name', 'nickname', 'author_userid', 'content', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True, read_only=True, source="comment_set")
    author_userid = UserSerializser(read_only=True)
    class Meta:
        model = Post
        fields = ['pk', 'name', 'nickname', 'author_userid',  'title', 'content', 'category','star_point',
                  'created_at', 'post_comment']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class Category_PostSerializer(serializers.ModelSerializer):
    post_list = PostSerializer(many=True, read_only=True, source="post_set")

    class Meta:
        model = Category
        fields = ['name', 'post_list']

