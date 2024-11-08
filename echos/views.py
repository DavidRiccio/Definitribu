# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import AddEchoForm, EditEchoForm
from .models import Echo

# Create your views here.


@login_required
def echo_list(request):
    all_echos = Echo.objects.all().order_by('-created_at')
    context = {'all_echos': all_echos}
    return render(request, 'echos/echo_list.html', context)


@login_required
def echo_detail(request, echo_pk):
    echo = Echo.objects.get(pk=echo_pk)
    waves = echo.waves.all()[:5]
    num_waves = waves.count()
    return render(
        request, 'echos/echo_detail.html', dict(echo=echo, waves=waves, num_waves=num_waves)
    )


@login_required
def echo_waves(request, echo_pk):
    echo = Echo.objects.get(pk=echo_pk)
    waves = echo.waves.all()
    return render(request, 'echos/echo_waves.html', dict(echo=echo, waves=waves))


@login_required
def add_echo(request):
    if request.method == 'GET':
        form = AddEchoForm()
    else:
        if (form := AddEchoForm(data=request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echo_list')
    return render(request, 'echos/add_echo.html', dict(form=form))


@login_required
def edit_echo(request, echo_pk):
    echo = Echo.objects.get(pk=echo_pk)
    if request.user != echo.user:
        return HttpResponseForbidden('NO ERES PROPIETARIO DE ESTE ECHO')
    if request.method == 'GET':
        form = EditEchoForm(instance=echo)
    else:
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save(commit=False)
            echo.save()
            return redirect('echos:echo_list')
    return render(request, 'echos/add_echo.html', dict(echo=echo, form=form))


@login_required
def delete_echo(request, echo_pk):
    echo = Echo.objects.get(pk=echo_pk)
    if request.user != echo.user:
        return HttpResponseForbidden()
    echo = Echo.objects.get(pk=echo_pk)
    echo.delete()
    return render(request, 'echos/delete_echo.html', dict(echo=echo))
