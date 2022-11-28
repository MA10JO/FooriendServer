from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    author_userid = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['post', 'author', 'author_userid', 'content', 'created_at']

    def get_author_userid(self, obj):
        return obj.author.userid


class PostSerializer(serializers.ModelSerializer):
    author_userid = serializers.SerializerMethodField()
    post_comment = CommentSerializer(many=True, read_only=True, source="comment_set")


    class Meta:
        model = Post
        fields = ['pk', 'author', 'author_userid', 'title', 'content', 'category',
                  'created_at', 'post_comment']

    def get_author_userid(self, obj):
        return obj.author.userid


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class Category_PostSerializer(serializers.ModelSerializer):
    post_list = PostSerializer(many=True, read_only=True, source="post_set")

    class Meta:
        model = Category
        fields = ['name', 'post_list']



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'userid']