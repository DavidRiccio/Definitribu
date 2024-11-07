from django.shortcuts import render
from .models import Wave
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Wave


@login_required
def wave_detail(request, wave_pk):
    # Obtiene el objeto Wave o devuelve un error 404 si no se encuentra
    wave = get_object_or_404(Wave, pk=wave_pk)
    
    # Renderiza la plantilla con el objeto wave
    return render(request, 'waves/wave_detail.html', {'wave': wave})