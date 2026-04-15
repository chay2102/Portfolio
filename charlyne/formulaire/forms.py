from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'country',
            'city',
            'home_address',
            'email',
            'phone_number',
            'service',
            'message',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'country': forms.Select(),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'home_address': forms.TextInput(attrs={'placeholder': 'Home address'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'service': forms.Select(),
            'message': forms.Textarea(attrs={'rows': 5, 'maxlength': 300}),
        }
