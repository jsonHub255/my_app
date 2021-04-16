from django import forms
from .models import Engin

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
