from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import SignupForm


# Create your views here.
def signup(request):
    form = SignupForm(request.POST or None)
    if (form := SignupForm(request.POST)).is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('echos:echo_list')
    return render(request, 'registration/signup.html', dict(form=form))


def logout_view(request):
    logout(request)
    return redirect('echos:echo_list')
