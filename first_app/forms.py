from django import forms


class UserCreationForm(forms.Form):
    user_name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Name',
                   'style': 'width: 300px',
                   'class': 'form-control'}
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'style': 'width: 300px',
                   'class': 'form-control'}),
        label="Password")
    email = forms.CharField(label="Email",
                            widget=forms.EmailInput(
                                attrs={'placeholder': 'email',
                                       'style': 'width: 300px',
                                       'class': 'form-control'})
                            )