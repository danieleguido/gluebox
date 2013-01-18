from django import forms

class SubscriberForm (forms.Form):
    first_name = forms.CharField( max_length = 64 ) # longer than standard field
    last_name = forms.CharField( max_length = 64 ) # longer than standard field
    email = forms.EmailField()
    affiliation = forms.CharField( max_length = 128 )
    accepted_terms = forms.BooleanField()
    description = forms.CharField() # personal description