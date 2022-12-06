from django import forms

class InputForm(forms.Form):

    nombre = forms.CharField(max_length = 10)
    email = forms.EmailField()