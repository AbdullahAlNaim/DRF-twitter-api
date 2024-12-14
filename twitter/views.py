from django.shortcuts import render
from rest_framework import generics
from .models import Tweets
from .serializers import TweetsSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.create_user(
    username='bob',
    email='bob@example.com',
    password='abc123'
)

token = Token.objects.create(user=user)

print(token.key)

# Create your views here.
class tweets(generics.ListCreateAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer

class OneTweet(generics.RetrieveDestroyAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer