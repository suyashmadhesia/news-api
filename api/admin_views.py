
from api.paginator import FeedPaginator
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from . models import Post
from . serializers import *


class AdminView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [BasicAuthentication]

    def post(self, request):
        raw_data = request.data
        data = {}
        try:
            data["post_id"] = news_id_generator()
            data["image_url"] = raw_data["image_url"]
            data["video_url"] = raw_data["video_url"]
            data["title"] = raw_data["title"]
            data["news_body"] = raw_data["news"]

            data["category"] = Category.objects.get(
                code_name=raw_data["category"])
        except:
            return Response({"message": " Error ! Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
        # print(data)
        serializer = AdminViewSerializer(data=data)
        if serializer.is_valid():
            Post.objects.create(**data)
            return Response({"message": "Posted !"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = request.data
        post = Post.objects.get(post_id=data['post_id'])
        comment = post.comments.all().order_by("created_at")
        if(len(comment) > 0):
            comment.delete()
        post.delete()
        return Response({"message": "Deleted !"}, status=status.HTTP_200_OK)

@method_decorator(never_cache, name="dispatch")
class AdminGetView(ListAPIView):
    permission_classes = [IsAdminUser]
    pagination_class = FeedPaginator
    serializer_class = AdminViewSerializer
    queryset = Post.objects.all()
