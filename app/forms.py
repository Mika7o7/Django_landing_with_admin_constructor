from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label="first_name", max_length=50)
    last_name = forms.CharField(label="last_name", max_length=50)
    phone = forms.CharField(label="phone", max_length=50)
