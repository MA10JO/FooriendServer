from rest_framework import serializers
from adv.models import Post, Comment

class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = ['state', 'title', 'category', 'party', 'content','author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content']