#pyordanov

from django import forms
from dim3app.models import UserAcc
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserAccForm(forms.ModelForm):
	class Meta:
		model = UserAcc
		fields = ('name','website', 'picture','interests')