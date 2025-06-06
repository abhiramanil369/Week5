from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers,generics,viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class RegisterView(generics.CreateAPIView):
    serializer_class=UserSerializer
    permission_classes=[AllowAny]


class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filter_fields=['author__username']

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
