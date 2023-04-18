from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import EmailValidator

from django import forms

from django.forms.widgets import PasswordInput, TextInput

#Registration form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].required = True

    # email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered')
        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long!')
        
         # validate email format
        validator = EmailValidator('Enter a valid email address.')
        try:
            validator(email)
        except forms.ValidationError:
            raise forms.ValidationError('Enter a valid email address.')

        return email
    
#Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')
            elif not user.is_active:
                raise forms.ValidationError('User account is not activated.')
        return cleaned_data
        
    
#update form
class UpdateUserForm(forms.ModelForm):
    password = None
    
    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].required = True
        
     # email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already registered')
        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long!')
        
         # validate email format
        validator = EmailValidator('Enter a valid email address.')
        try:
            validator(email)
        except forms.ValidationError:
            raise forms.ValidationError('Enter a valid email address.')

        return email