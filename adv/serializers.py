from rest_framework import serializers
from adv.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content']


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['state', 'title', 'category', 'party', 'content', 'author']
