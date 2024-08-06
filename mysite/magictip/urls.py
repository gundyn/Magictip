from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card_image/', views.card_image, name='card_image'),
]