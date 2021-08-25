from django.urls import path
from .views import BlogDetailView, BlogListView, CategoryDetailView, CategoryListView

app_name = "blog_api"

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list"),
    path('<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('category', CategoryListView.as_view(), name="category_list"),
    path('category/<int:pk>', CategoryDetailView.as_view(), name="category_detail"),
]
