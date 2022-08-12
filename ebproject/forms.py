from django import forms

class InputForm(forms.Form):

    name = forms.CharField(max_length = 250)
    phone = forms.CharField(max_length = 50)
    email = forms.CharField(max_length = 250)
    message = forms.CharField(max_length = 500, widget=forms.Textarea)
    public_id = forms.CharField(max_length = 250, label="Property Id" )