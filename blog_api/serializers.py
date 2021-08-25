from rest_framework import serializers
from blog.models import Category, Blog
from user.serializers import UserTopSerializer


class BlogTopSerilizer(serializers.ModelSerializer):
    author = UserTopSerializer(many=False, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'post', 'author')


class CategoryTopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializers(serializers.ModelSerializer):
    blogs = BlogTopSerilizer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'blogs')


class BlogsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title', 'post', 'category', 'author',
                  'excerpt', 'published_on', 'slug', 'status',)


class BlogSerializers(serializers.ModelSerializer):
    category = CategoryTopSerializer(many=False, read_only=True)
    author = UserTopSerializer(many=False, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'post', 'category', 'author',
                  'excerpt', 'published_on', 'slug')
