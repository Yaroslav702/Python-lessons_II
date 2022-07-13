from django.urls import include, path
from snippets import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'snippets', views.SnippetsViewSet, basename='snippets')
router.register(r'users', views.UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]

