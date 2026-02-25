from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('add_job/', views.add_job, name='add_job'),
    path ('all_jobs/', views.all_jobs, name='all_jobs'),
]