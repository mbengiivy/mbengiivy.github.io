from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main portfolio page
    path('project/<int:project_id>/', views.project_detail, name='project_detail'), # Project detail page
]