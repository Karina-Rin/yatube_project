from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path("", views.index),
    # Список мороженого
    path("posts/", views.group_posts),
    # Подробная информация о постах. Ждем пременную типа slug
    path("group/<slug:slug>/", views.group_posts),
]
