from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
]
