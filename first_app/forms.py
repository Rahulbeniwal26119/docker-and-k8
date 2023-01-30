from django import forms
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

# class UserCreationForm(forms.Form):
#     user_name = forms.CharField(
#         label="Name",
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Name',
#                    'style': 'width: 300px',
#                    'class': 'form-control'}
#         ))
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#         attrs={'placeholder': 'Password',
#                'style': 'width: 300px',
#                    'class': 'form-control'}),
#         label="Password")
#     email = forms.CharField(label="Email",
#                             widget=forms.EmailInput(
#                                 attrs={'placeholder': 'email',
#                                        'style': 'width: 300px',
#                                        'class': 'form-control'})
#                             )


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'user_info']