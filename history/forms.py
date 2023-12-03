from django import forms
from .models import Units, Notes


class UnitForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = ['unitName']
        labels = {
            'unitName': 'Nazwa działu'
        }

        widgets = {
            'unitName': forms.TextInput(attrs={'placeholder': 'Podaj nazwę działu', 'class': 'form-input'})
        }
        

class NoteForm(forms.ModelForm):    
    class Meta:
        model = Notes
        fields = ['noteTitle', 'noteContent']
        labels = {
            'noteTitle': 'Tytuł',
            'noteContent': 'Notatka'
        }

        widgets = {
            'noteTitle': forms.TextInput(attrs={'placeholder': 'Podaj tytuł notatki', 'class': 'form-input'}),
            'noteContent': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'Wpisz swoją notatke', 'class': 'form-textarea'})
        }
        