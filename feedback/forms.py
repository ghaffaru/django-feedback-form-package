from django import forms

class FeedbackForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))