# student_project_management/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),  # Подключаем маршруты приложения `projects` как главные маршруты

]
