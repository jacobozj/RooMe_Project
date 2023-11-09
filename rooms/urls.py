from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.room, name='room'),
    path('about/', views.about, name='about'),
    path('reserva/<int:id>', views.booking, name='reserva'),
    path('delete_room/', views.delete_room, name='delete_room'),
    path('detele_account/', views.delete_account, name='delete_account'),
    path('comentario/<int:id>', views.comentario, name='comentario')
]