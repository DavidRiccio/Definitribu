from django.contrib.auth.decorators import login_required
from 
# Create your views here.
from django.shortcuts import redirect, render

from .models import Wave


@login_required
def wave_detail(request, wave_pk):
    wave = Wave.objects.get(Wave, pk=wave_pk)

    return render(request, 'waves/wave_detail.html', {'wave': wave})


@login_required
def edit_wave(request):
    pass


@login_required
def add_wave(request):
    if request.method == 'GET':
        form = AddWaveForm()
    else:
        if (form := AddWaveForm(data=request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echo_list')
    return render(request, 'echos/add_echo.html', dict(form=form))


@login_required
def delete_wave(request):
    pass
