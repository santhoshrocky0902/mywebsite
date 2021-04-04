from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(label ='', widget = forms.EmailInput(attrs ={'placeholder':'Your Email', 'class':'form-control'}))
    class Meta:
        model = Subscriber
        fields = ['email'] 

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        qs = Subscriber.objects.filter(email__iexact= email)
        return email