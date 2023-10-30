from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.room, name='room'),
    path('about/', views.about, name='about'),
    path('reserva/<int:id>', views.booking, name='reserva')
]