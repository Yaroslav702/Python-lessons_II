from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from blog.serializers import UserSerializer, GroupSerializer
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})





def post_like(request, pk):
    post = Post.objects.get(id=pk)
    post.likes += 1
    post.save()
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]