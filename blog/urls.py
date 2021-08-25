from django.urls import path
from .views import homePageView

app_name="blog"

urlpatterns = [
    path('', homePageView, name="home")
]
