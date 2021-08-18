import json
from django.db.models.query import QuerySet

from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from . models import Post
from . serializers import *

# Create your views here.

class HomeView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        data = Post.objects.all()
        serializers = NewsSerializer(data, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class SingleNewsView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(post_id=pk)
            serializers = SingleNewsSerializer(post)
        except:
            return Response({"Message" : "Data Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializers.data, status=status.HTTP_200_OK)


class CommentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        post = Post.objects.get(post_id = data["post_id"])
        data["comment_id"] = comment_id_generator()
        serializer = CommentSerializer(data = data)
        if serializer.is_valid():
            post.comments.create(**serializer.data)
            return Response({'message': 'Comment Done'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data
        comment = Comment.objects.get(comment_id = data["command_id"])
        comment.delete()
        return Response({"Message" : "Comment Deleted"}, status=status.HTTP_200_OK)



class FetchComments(APIView):
    permission_classes = [AllowAny]


    def get(self ,request, pk):
        try:
            comments = Post.objects.get(post_id=pk).comments.all()
            serializers = CommentSerializer(comments, many=True)
        except:
            return Response({"error" : "No Comments founds"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializers.data, status=status.HTTP_200_OK)


class AdminView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        posts = Post.objects.all()
        serializer = AdminViewSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        raw_data = request.data
        data = {}
        data["post_id"] = news_id_generator()
        data["image_url"] = raw_data["image_url"]
        data["video_url"] = raw_data["video_url"]
        data["title"] = raw_data["title"]
        data["news_body"] = raw_data["news"]
        data["category"] = Category.objects.get(code_name=raw_data["category"])
        print(data)
        serializer = AdminViewSerializer(data = data)
        if serializer.is_valid():
            Post.objects.create(**data)
            return Response({"message" : "Posted !"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

    def delete(self, request):
        data = request.data
        post = Post.objects.get(post_id = data['post_id'])
        comment = post.comments.all()
        if(len(comment) > 0):
            comment.delete()
        post.delete()
        return Response({"Message" : "Deleted !"}, status=status.HTTP_200_OK)

