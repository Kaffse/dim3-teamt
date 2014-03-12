from aggressiveBackpack.models import UserProfile, Project, List, Task
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'friends', 'projects')


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('owner', 'name', 'description', 'website', 'tags')
