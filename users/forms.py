from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from django.core.validators import MinLengthValidator

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        validators=[MinLengthValidator(4)],  # Ensure a minimum length of 4
    )
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    # password1 = forms.CharField()
    # password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProfForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'location', 'user_type']
