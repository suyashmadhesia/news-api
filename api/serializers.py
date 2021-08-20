from django.db.models import fields
from . models import *
from . utils import *
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'post_id',
            'title',
            'category',
            'news_body',
            'image_url',
            'video_url',
            'created_at',
        ]
        


class SingleNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


class AdminViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'post_id',
            'title',
            'category',
            'news_body',
            'image_url',
            'video_url',
            'created_at',
            'comments',
        ]
        depth = 1