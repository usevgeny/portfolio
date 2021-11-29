
from django import forms





class EmailForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    mail = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Contact E-mail'}))
    mobile_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Mobile Number'}))
    message_text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Message'})) #'readonly': True}))
    # fields=['driver_pk', 'column_numb