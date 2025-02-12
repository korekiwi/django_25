from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from unidecode import unidecode
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:tag_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг", blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", related_name="posts", default=None, null=True)
    tags = models.ManyToManyField("Tag", related_name="posts", verbose_name="Теги")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="posts",
        default=None,
        verbose_name="Категория",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг")
    description = models.TextField(
        blank=True, null=True, default="Без описания", verbose_name="Описание"
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog:category_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]