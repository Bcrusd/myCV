from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'mail@ornek.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesaj...', 'rows': 4}),
        }
