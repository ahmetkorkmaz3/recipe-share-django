from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']
            if password == password_again:
                signup = User.objects.create(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                signup.save()
                return redirect('login')
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {
            'form': form,
            'title': 'Sign Up'
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
