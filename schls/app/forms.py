
from django import forms
from .models import Applymodel
from .models import coursedetails# Make sure this matches your model name exactly
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForms(UserCreationForm):
    email=forms.EmailField(required=True)
    phone=forms.CharField(max_length=10)
    class Meta:
        model=User
        fields = ("username", "email", "phone", "password1","password2")
        
class courseForm(forms.ModelForm):
    class Meta:
        model = Applymodel
        fields = ("name", "email", "phone", "passyear","selectcourse")
        
class createForm(forms.ModelForm):
    
    class Meta:
        model = coursedetails
        fields = ("name", "durations", "fees", "description")

