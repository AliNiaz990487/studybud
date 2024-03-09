from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("room_page/<str:pk>/", views.room, name='room'), # pk for primary key,
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
]