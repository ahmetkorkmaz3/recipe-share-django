from django import forms


class CustomUserCreationForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=255,
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=255,
    )
    username = forms.CharField(
        label='Username',
        min_length=4,
        max_length=255,
    )
    email = forms.EmailField(
        label='Email',
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password_again = forms.CharField(
        label='Password Again',
        widget=forms.PasswordInput,
    )
