from unicodedata import category
from urllib.request import Request
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})


class PostDetail(generics.GenericAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'post':self.object}, template_name='post_page.html')


class CategoryPosts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get_objects(self, pk):
        try:
            return Post.objects.filter(category__id = pk)
        except:
            raise Http404
            


    def get(self, request, pk, *args, **kwargs):
        self.posts = self.get_objects(pk)
        return Response({'cat_posts': self.posts}, template_name='category_posts.html')


class PostLike(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        post.set_like()
        return redirect("/")


class PostDislike(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        post.set_dislike()
        return redirect("/")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]