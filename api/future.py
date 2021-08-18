from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .utils import get_ist

class AccountManager(BaseUserManager):

    def create_user(self, account_id, password, **extra_fields):
        account = self.model(account_id, **extra_fields)
        account.set_password(password)
        account.save()


class Account(AbstractBaseUser, PermissionsMixin):
    account_id = models.CharField(
        max_length=20, default='account_id', primary_key=True
    )
    id_type = models.CharField(max_length=6, default='EMAIL')
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    joined_at = models.DateTimeField(default=get_ist())
    USERNAME_FIELD = 'account_id'
    REQUIRED_FIELDS = ('joined_at', 'id_type')

    objects = AccountManager()


# TODO this class is for implementing all the comment operations
# in which sending data in get request using json
#class Comment(APIView):
#     permission_classes = [AllowAny]


#     def get(self ,request, pk):
#         try:
#             comments = Post.objects.get(post_id=pk).comments.all()
#             serializers = CommentSerializer(comments, many=True)
#         except:
#             return Response({"error" : "No Comments founds"}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializers.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         # data = json.loads(request.data)
#         # print(request.data)
#         post = Post.objects.get(post_id = request.data["post_id"])
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.data)
#             # comment = Comment.objects.get(comment_id=request.data["comment_id"])
#             post.comments.create(**serializer.data)
#             return Response({'message': 'Comment Done'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)