from django.shortcuts import render

# Create your views here.

# class HomePageView(): 

def homePageView(request):
    return render(request, 'blog/home.html')
