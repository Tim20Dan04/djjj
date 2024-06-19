# projects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('add/', views.add_project, name='add_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),  # новый URL для редактирования проекта
]
