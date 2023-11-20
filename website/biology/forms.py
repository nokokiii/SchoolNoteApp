from django import forms
from .models import Units, Notes


class UnitForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = ['unitName']
        

class NoteForm(forms.ModelForm):    
    class Meta:
        model = Notes
        fields = ['noteTitle', 'noteContent']
        labels = {
            'noteTitle': 'Title',
            'noteContent': 'Notes'
        }
        widgets = {
            'noteTitle': forms.TextInput(attrs={'placeholder': 'Enter note title here'}),
            'noteContent': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'Enter your notes here'})
        }
        