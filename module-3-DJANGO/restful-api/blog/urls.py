from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_like/<int:pk>', views.PostLike.as_view(), name='post_like'),
    path('post_dislike/<int:pk>', views.PostDislike.as_view(), name='post_dislike'),
    path('', include(router.urls)),
    path('page/<int:pk>', views.PostDetail.as_view(), name='page'),
    path('category/<int:pk>', views.CategoryPosts.as_view(), name='category'),
    path('api-auth/', include('rest_framework.urls'), name='urls'),
]