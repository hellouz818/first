from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('home/', views.home, name='home'),
]