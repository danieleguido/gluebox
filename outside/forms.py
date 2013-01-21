from django import forms
from captcha.fields import CaptchaField

class SubscriberForm (forms.Form):
    first_name = forms.CharField( max_length = 64 ) # longer than standard field
    last_name = forms.CharField( max_length = 64 ) # longer than standard field
    email = forms.EmailField()
    affiliation = forms.CharField( max_length = 128, required=False )
    accepted_terms = forms.BooleanField()
    description = forms.CharField( widget=forms.Textarea) # personal description

class LoginForm( forms.Form ):
	username = forms.CharField( max_length=32, widget=forms.TextInput )
	password = forms.CharField( max_length=64, label='Password', widget=forms.PasswordInput(render_value=False ) )
