from django.urls import path
from api.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('<str:pk>', NewsViewByCategory.as_view(), name='Category View'),
    path('news/<str:pk>', SingleNewsView.as_view(), name='Posts'),
    path("news/<str:pk>/comment", FetchComments.as_view(), name="Fetch Comment"),
    path('post_comment/news', CommentView.as_view(), name='Comment'),
    path('site-admin/news', AdminView.as_view(), name='Site Admin View')
]
