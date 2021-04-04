from django import forms
from .models import Admission

class ProfileForm(forms.Form):
   picture = forms.ImageField() 