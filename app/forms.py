from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField(
        min_length=4,
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        min_length=2,
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    second_name = forms.CharField(
        min_length=2,
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
