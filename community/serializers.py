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
        fields = ['author', 'author_userid', 'title', 'content', 'category',
                  'created_at', 'post_comment']

    def get_author_userid(self, obj):
        return obj.author.userid


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'userid']