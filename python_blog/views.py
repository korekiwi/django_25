from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import Count, F

from posts_dataset import dataset
from help_functions import python_slugify, python_slugify_list

from python_blog.models import Post, Category, Tag

CATEGORIES = [
    {"slug": "python", "name": "Python"},
    {"slug": "django", "name": "Django"},
    {"slug": "postgresql", "name": "PostgreSQL"},
    {"slug": "docker", "name": "Docker"},
    {"slug": "linux", "name": "Linux"},
]


def main(request):

    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_status": "moderator",
    }
    return render(request, "main.html", context)


def about(request):
    context = {
        "title": "О проекте",
        "project_information": "Информация о проекте",
        "contact": "Контактные данные",
    }

    return render(request, "about.html", context)


def catalog_posts(request):

    context = {
        "title": "Каталог постов",
        "posts": Post.objects.select_related('category', 'author').prefetch_related('tags').all(),
    }
    
    return render(request, "catalog_posts.html", context)


def post_detail(request, post_slug):
    post = Post.objects.select_related("category", "author").prefetch_related("tags").get(slug=post_slug)

    session = request.session
    key = f"viewed_posts_{post.id}"

    if key not in session:
        Post.objects.filter(id=post.id).update(views=F("views") + 1)
        session[key] = True
        post.refresh_from_db()

    context = {
        "post": post,
        }
    return render(request, "post_detail.html", context)


def catalog_categories(request):
    context = {
        "title": "Категории",
        "categories": Category.objects.annotate(posts_count=Count("posts")).order_by("-posts_count")
    }
    return render(request, "catalog_categories.html", context)


def category_detail(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = category.posts.select_related('category', 'author').prefetch_related('tags').all()

    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "category_detail.html", context)


def catalog_tags(request):
    context = {
        'title': 'Теги',
        'tags': Tag.objects.annotate(posts_count=Count("posts")).order_by("-posts_count")
    }

    return render(request, "catalog_tags.html", context)


def tag_detail(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = tag.posts.select_related('category', 'author').prefetch_related('tags').all()

    context = {
        "title": f"Посты по тегу {tag.name}",
        "tag": tag,
        "posts": posts,
    }

    return render(request, "tag_detail.html", context)
