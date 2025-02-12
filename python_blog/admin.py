from django.contrib import admin
from python_blog.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ["title", "published_date", "updated_date", "category"]
    readonly_fields = ["slug"]

@admin.register(Category)
class PostCategory(admin.ModelAdmin):
    search_fiels = ['name', 'description']
    list_display = ['name']
    readonly_fields = ['slug']

@admin.register(Tag)
class PostTag(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    readonly_fields = ['slug']
