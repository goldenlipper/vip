from django.urls import path

from . import views

app_name='vips'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:client_id>/<str:level_number>/clients/', views.clients, name='clients'),
    path('<int:client_id>/<str:level_number>/dashboard/', views.dashboard, name='dashboard'),
    path('<int:client_id>/<str:level_number>/profile/', views.profile, name='profile'),
    path('<str:vip1_name>/vip2/', views.vip2, name='vip2'),
]
