
from django import forms
from django.core.exceptions import ValidationError
import re




class EmailForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    mail = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Contact E-mail'}))
    mobile_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    message_text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Message'})) #'readonly': True}))
    # fields=['driver_pk', 'column_numb



class SendChatForm(forms.Form):
    fields = ['name', 'telephone', 'message']
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    telephone = forms.CharField(required=True, max_length=20 , widget=forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Message'}))
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if re.match(r'^\+?1?\d{9,15}$', telephone):
            return telephone
        else:
            raise ValidationError('Format: +9999999999, max: 15 characters')


