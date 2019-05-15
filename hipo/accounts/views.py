from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {
        'title': 'Profile',
        'user': user,
    })

def dashboard(request):
    return render(request, 'dashboard.html', {
        'title': 'Profile Page'
    })
