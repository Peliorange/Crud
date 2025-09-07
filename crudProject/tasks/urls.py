from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.task_form, name="task_form"),
    path("api/tasks/", views.taskApi, name="task_api"),
    path("api/tasks/<int:pk>/", views.taskApi, name="task_detail"),  # Añadir esta línea
]
