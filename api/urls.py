from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, PostViewSet, CommentViewSet,
    RegisterView, login_view
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("users/register/", RegisterView.as_view(), name="register"),
    path("users/login/", login_view, name="login"),
    path("", include(router.urls)),
]
