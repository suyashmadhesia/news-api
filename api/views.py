
import re
from typing import Tuple
from rest_framework.pagination import CursorPagination
from api.paginator import FeedPaginator

from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . models import Post
from . serializers import *


@method_decorator(never_cache, name="dispatch")
class HomeView(ListAPIView):
    permission_classes = [AllowAny]
    # authentication_classes = [AllowAny]
    pagination_class = FeedPaginator
    serializer_class = NewsSerializer
    queryset = Post.objects.all()


class SingleNewsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            post = Post.objects.filter(post_id=pk)
            serializer = SingleNewsSerializer(post, many=True)
        except:
            return Response({"Message": "Data Not Found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            post = Post.objects.get(post_id=data["post_id"])
        except:
            return Response({'message': 'Error Post Id is not Given or Post Id is worng'}, status=status.HTTP_400_BAD_REQUEST)
        data["comment_id"] = comment_id_generator()
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            post.comments.create(**serializer.data)
            return Response({'message': 'Comment Done'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsViewByCategory(GenericAPIView):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    queryset = None
    pagination_class = FeedPaginator
    

    def get(self, request, pk):
        self.queryset = Post.objects.filter(category__code_name=pk)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = NewsSerializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            return Response(result.data)
