from django.urls import path
from . import views

app_name = 'waves'

urlpatterns = [
    path('<int:wave_pk>/', views.wave_detail, name='wave_detail'),  # Asegúrate de que el nombre del parámetro sea correcto
]