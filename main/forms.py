from django import forms
from .models import Contact, Track, Subscription

class ContactForm(forms.ModelForm):
	name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
	email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
	website = forms.CharField(required=True, label='Website', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'}))
	phone = forms.IntegerField(required=True, label='Phone', widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Phone'}))
	message = forms.CharField(required=True, label='message', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}))

	class Meta:
		model = Contact
		fields =['name', 'email', 'phone', 'website', 'message']

class TrackForm(forms.ModelForm):
	bill = forms.IntegerField(required=True, label='Bill', widget=forms.NumberInput(attrs={'class': 'form-control',}))

	class Meta:
		model = Track
		fields = ['bill']

class SubscriptionForm(forms.ModelForm):
	email = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

	class Meta:
		model = Subscription
		fields = ['email']