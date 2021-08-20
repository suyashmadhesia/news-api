

from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView


from rest_framework.permissions import IsAdminUser
from . serializers import *
from . models import Category


class CategoryView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    queryset = Category.objects.all()
