from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'input username', 'placeholder': 'Email'})) 
    first_name = forms.CharField(label='First Name', max_length="100", widget=forms.TextInput(attrs={'class': 'input username', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='last Name', max_length="100", widget=forms.TextInput(attrs={'class': 'input username', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input username'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['label'] = 'Username'

        self.fields['password1'].widget.attrs['class'] = 'input username'
        self.fields['password1'].widget.attrs['placeholder'] = '********'
        self.fields['password1'].widget.attrs['label'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'input username'
        self.fields['password2'].widget.attrs['placeholder'] = '********'
        self.fields['password2'].widget.attrs['label'] = 'Confirm Password'