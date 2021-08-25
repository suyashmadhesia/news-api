from api.category_view import CategoryView
from api.admin_views import AdminGetView, AdminView
from django.urls import path
from api.views import *

urlpatterns = [
    path('news', HomeView.as_view(), name='Home'),
    path('cat/news/<str:pk>', NewsViewByCategory.as_view(), name='News Category View'),
    path('news/<str:pk>/comment', FetchComments.as_view(), name="Fetch Comment"),
    path('post_comment/news', CommentView.as_view(), name='Post Comment'),
    path('site-admin/post', AdminView.as_view(), name='Admin Post'),
    path('site-admin/get', AdminGetView.as_view(), name='Admin Get'),
    path('site-admin/category', CategoryView.as_view(), name='Category')
]
