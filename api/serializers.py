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
