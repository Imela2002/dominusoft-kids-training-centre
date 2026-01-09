from wsgiref.validate import validator

from django import forms
from django.core.validators import EmailValidator

from .models import ContactMessage


class ContactForm(forms.ModelForm):
#     emri = forms.CharField(max_length=50)
#     mbiemri = forms.CharField(max_length=50)
#     email = forms.CharField(validators=[EmailValidator()])
#     mesazhi juaj = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = ContactMessage
        fields = "__all__"