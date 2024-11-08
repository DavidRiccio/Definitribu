from django.urls import path

from . import views

app_name = 'echos'


urlpatterns = [
    path('', views.echo_list, name='echo_list'),
    path('<int:echo_pk>/', views.echo_detail, name='echo_detail'),
    path('add/', views.add_echo, name='add_echo'),
    path('<int:echo_pk>/waves/', views.echo_waves, name='echo_waves'),
    path('<int:echo_pk>/edit/', views.edit_echo, name='edit_echo'),
    path('<int:echo_pk>/delete/', views.delete_echo, name='delete_echo'),
]
