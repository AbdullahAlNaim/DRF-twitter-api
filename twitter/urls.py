from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweets.as_view(), name='tweets'),
    path('tweet/<int:pk>', views.OneTweet.as_view(), name='post')
]