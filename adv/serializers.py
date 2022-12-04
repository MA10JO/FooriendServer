from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'nickname', 'content', 'created_at']




class PostSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True, read_only=True, source="comment_set")

    class Meta:
        model = Post
        fields = ['pk', 'name', 'nickname', 'title', 'content', 'category', 'state', 'party',
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

