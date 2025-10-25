from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Category, Post, Comment
from .serializers import (
    CategorySerializer, PostSerializer, CommentSerializer,
    UserSerializer, RegisterSerializer
)
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

# Registration and login endpoints
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)
        user = User.objects.get(id=resp.data["id"])
        token, _ = Token.objects.get_or_create(user=user)
        data = {"user": UserSerializer(user).data, "token": token.key}
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": UserSerializer(user).data})

# ViewSets
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author", "category").all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "category__id", "author__id"]
    search_fields = ["title", "content", "author__username"]
    ordering_fields = ["created_at", "published_at", "title"]

    def perform_create(self, serializer):
        if not self.request.user or not self.request.user.is_authenticated:
            raise permissions.PermissionDenied("Authentication required to create posts")
        serializer.save(author=self.request.user)

    @action(detail=False, methods=["get"], url_path="by-author/(?P<username>[^/.]+)")
    def by_author(self, request, username=None):
        user = get_object_or_404(User, username=username)
        qs = self.filter_queryset(self.get_queryset().filter(author=user))
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="by-category/(?P<slug>[^/.]+)")
    def by_category(self, request, slug=None):
        cat = get_object_or_404(Category, slug=slug)
        qs = self.filter_queryset(self.get_queryset().filter(category=cat, status="published"))
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post").all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
