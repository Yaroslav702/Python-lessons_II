from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('groups', views.GroupView)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_like/<int:pk>', views.post_like, name='post_like'),
    path('check', include('rest_framework.urls'), name='urls')
    # path('post-dislike/<int:pk>', views.PostDislike, name='post_dislike')
]   
