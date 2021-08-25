from django.test import TestCase
from .models import Blog, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryCreate(TestCase):
    def test_category_create(self):
        category = Category.objects.create(name="test")
        self.assertEqual(category.name, 'test')
        self.assertEqual(str(category), 'test')


class BlogCreate(TestCase):
    def test_blog_create(self):
        user = User.objects.create_user(
            email="test@test.com", password="password", first_name="test", last_name="user")
        category = Category.objects.create(name="test")
        blog = Blog.objects.create(title='title', post="test post",
                                   slug="slug", excerpt="test post", author=user, category=category)

        self.assertEqual(str(blog), 'title')
        self.assertEqual(blog.author, user)
        self.assertEqual(blog.category, category)
        self.assertEqual(blog.post, 'test post')
        self.assertEqual(blog.slug, 'slug')
        self.assertEqual(blog.excerpt, 'test post')
