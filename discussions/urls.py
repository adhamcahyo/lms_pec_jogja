from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion_list, name='discussion_list'),
    path('<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
    path('create/', views.create_discussion, name='create_discussion'),
    # Add more URLs for other discussion-related views as needed
]
