from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Record

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

class NewRecord(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'phone': forms.TextInput(attrs={'class': 'input'}),
            'address': forms.TextInput(attrs={'class': 'input'}),
            'city': forms.TextInput(attrs={'class': 'input'}),
            'state': forms.TextInput(attrs={'class': 'input'}),
            'zipcode': forms.TextInput(attrs={'class': 'input'}),
        }