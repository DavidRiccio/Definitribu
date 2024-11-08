from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('<int:wave_pk>/', views.wave_detail, name='wave_detail'),
    path('<int:wave_pk>/add', views.add_wave, name='add_wave'),
    path('<int:wave_pk>/edit', views.add_wave, name='add_wave'),
    path('<int:wave_pk>/delete', views.delete_wave, name='delete_wave'),
]
