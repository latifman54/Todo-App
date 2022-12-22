from django import forms
from django.contrib.auth.models import User

from .models import Task


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255, widget=forms.PasswordInput)


# class SignUpForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255, widget=forms.PasswordInput)
#     password_confirm = forms.CharField(max_length=255, widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")

#         if password != password_confirm:
#             raise forms.ValidationError(
#                 "The two password fields didn't match."
#             )


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['text']
#         widgets = {'text': forms.TextInput(attrs={'placeholder': 'Add a new task...'})}

