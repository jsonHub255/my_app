from django import forms
from .models import Engin, Driver

class EnginForm(forms.ModelForm):
    eng_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'placeholder': 'Engin Name',
            'id': 'eng_name',
            'class': 'eng_name_cls'
            }
        ))

    eng_code = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'placeholder': 'Code',
            'id': 'eng_code'
            }
        ))
    class Meta:        
        model = Engin
        fields = [
            'eng_name',
            'eng_code'
        ]


class DriverForm(forms.ModelForm):
    driv_full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'placeholder': 'Full Name',
            'id': 'driv_name'
        }
    ))

    class Meta:
        model = Driver
        fields = [
            'driv_eng',
            'driv_full_name'
        ]
