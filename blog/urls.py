# blog\urls.py ГЛАВНЫЙ
from django.contrib import admin
from django.urls import path
from python_blog.views import main, about
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
"""
Конверторы путей Django:
str - строки, любые символы кроме слэша '/' (по умолчанию)
int - положительные целые числа включая 0
slug - ASCII буквы/цифры, дефисы и подчеркивания
uuid - уникальные идентификаторы UUID пример '075194d3-6885-417e-a8a8-6c931e272f00'
path - строки, включая слэши '/'

Пример использования:
path('articles/<int:year>/', views.year_archive)
path('blog/<slug:post_slug>/', views.post_detail)

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name="main"),
    path("about/", about, name="about"),

    # Подключаем python_blog.urls
    path('posts/', include('python_blog.urls'), name='posts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]