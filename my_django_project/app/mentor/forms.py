from django import forms
from .models import Mentor

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['bio', 'expertise', 'years_of_experience', 'hourly_rate', 'is_available']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'hourly_rate': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
            'years_of_experience': forms.NumberInput(attrs={'min': '0'}),
        } 