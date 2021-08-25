from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):

    class BlogObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Blog.PUBLISHED)

    PUBLISHED = 'published'
    DRAFT = 'draft'

    STATUS_CHOICES = (
        (PUBLISHED, 'published'),
        (DRAFT, 'draft')
    )

    category = models.ForeignKey(
        Category, related_name='blogs', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(null=True, blank=True, default=None)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blogs")
    status = models.CharField(choices=STATUS_CHOICES,
                              default=PUBLISHED, max_length=20)
    slug = models.SlugField(max_length=100)
    objects = models.Manager()
    blog_object = BlogObject()

    class meta:
        ordering = ('-created_at')

    def __str__(self):
        return self.title
