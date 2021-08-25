from django.contrib import admin
from .models import Blog, Category

# Register your models here.


class customBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author', 'category')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, customBlogAdmin)
admin.site.register(Category)
