from django.contrib.auth.forms import userCreationForm
from django.contrib.auth.models import User

from django import forms

class CreateUserForm(userCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
        
    def __ini__(self, *args, **kwargs):
        super(CreateUserForm).__init__(*args, **kwargs)

    #email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is invalid')
        if len(email > 350):
            raise forms.ValidationError('Your email is too long!')