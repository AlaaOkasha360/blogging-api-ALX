from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PostViewSet, CommentViewSet, register_user, login_user

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('users/register/', register_user),
    path('users/login/', login_user),
    path('', include(router.urls)),
]
