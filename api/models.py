from api.utils import get_ist
from django.db import models


class Category(models.Model):
    code_name = models.CharField(max_length=2, default='', primary_key=True)
    name = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    comment_id = models.CharField(max_length=30, default='', primary_key=True)
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False, default='')
    created_at = models.DateTimeField(default=get_ist())
    comment = models.TextField(blank=False)

    def __str__(self) -> str:
        return self.comment_id


class Post(models.Model):
    post_id = models.CharField(max_length=22, primary_key=True, default='')
    title = models.CharField(max_length=120, blank=False)
    category = models.ForeignKey(
        Category, blank=True, related_name='news_category', on_delete=models.CASCADE, default='')
    news_body = models.TextField(blank=True)
    image_url = models.CharField(max_length=150, blank=True, default='')
    video_url = models.CharField(max_length=150, blank=True, default='')
    created_at = models.DateTimeField(default=get_ist())
    comments = models.ManyToManyField(
        Comment, blank=True, related_name='news_comment', default='')

    
    def __str__(self) -> str:
        return self.title
