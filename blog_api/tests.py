from datetime import datetime
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from blog.models import Blog, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogListTest(APITestCase):
    def test_blog_list(self):
        url = reverse('blog_api:blog_list')
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_create(self):
        url = reverse('blog_api:blog_list')
        category = Category.objects.create(name="test")
        user = User.objects.create_user(
            email="test@test.com", password="password", first_name='test', last_name="user")
        data = {"title": 'title', "post": 'test post', "slug": 'slug',
                "excerpt": 'test_post', "author": user.id, "category": category.id}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(email=user.email, password='password')

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_blog_update(self):
        client = APIClient()
        category = Category.objects.create(name="django")
        user1 = User.objects.create_user(
            email="user1@test.com", password="password", first_name="user", last_name="One")
        user2 = User.objects.create_user(
            email="user2@test.com", password="password", first_name="user", last_name="Two")
        blog = Blog.objects.create(title="test blog", post="test post",
                                   excerpt="test blog", slug="test_slug", author=user1, category=category)
        client.login(email=user1.email, password='password')

        url = reverse(('blog_api:blog_detail'), kwargs={'pk': blog.id})

        response = client.put(url, {
            "title": "hello world test",
            "post": "something to test only",
            "excerpt": "something to test only",
            "published_on": "2021-07-30T18:58:00Z",
            "slug": "somehtinf",
            "status": "published"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
