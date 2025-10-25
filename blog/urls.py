from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("blog.urls")),
    # optional schema / docs endpoints
    path("openapi/", get_schema_view(title="Blog API", description="API for blog", version="1.0.0"), name="openapi-schema"),
]
