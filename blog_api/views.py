from blog.models import Blog, Category
from rest_framework import generics
from .serializers import BlogsSerializers, CategorySerializers, BlogSerializers
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, SAFE_METHODS


class UserPostPermisssions(BasePermission):
    message = "You dont have the permissions to view the data"

    def has_object_permission(self, request, view, obj):
        if (request.method in SAFE_METHODS):
            return True

        return obj.author == request.user or request.user.is_superuser


class BlogListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.blog_object.all()
    serializer_class = BlogsSerializers


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView, UserPostPermisssions):
    permission_classes = [UserPostPermisssions]
    queryset = Blog.blog_object.all()
    serializer_class = BlogSerializers


class CategoryListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
