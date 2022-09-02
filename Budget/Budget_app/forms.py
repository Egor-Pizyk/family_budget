from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from Budget_app.models import CategoriesList, CountsList, CountValues
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = CategoriesList
        fields = ('category_name', 'transaction_type')


class CreateCountForm(forms.ModelForm):
    class Meta:
        model = CountsList
        fields = ('count_name', 'balance', 'card_number')


class CreateCountValueForm(forms.ModelForm):
    class Meta:
        model = CountValues
        fields = ('count_list_id', 'transaction_type', 'transaction_value', 'description', 'category', 'currency')


class CreateTransferToCard(forms.Form):
    from_count = forms.CharField(max_length=255)
    to_count = forms.CharField(max_length=255)
    transaction_value = forms.FloatField()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label='Username', error_messages={
            'unique': _("Користувач з таким іменем вже існує."),
        })
    email = forms.EmailField(max_length=30, required=True, label='Email', error_messages={'wrong': _("Невірний формат email.")})
    password1 = forms.CharField(max_length=30, min_length=8, required=True, label='Password')
    password2 = forms.CharField(max_length=30, min_length=8, required=True, label='Password confirmation')

    error_messages = {
        'password_mismatch': _(
            "Паролі не співпадають."
        ),
    }

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Користувач з таким email вже існує.")
        return data

    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['email'].lower()
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True)

    error_messages = {
        'invalid_login': _(
            "Введіть правильний логін і пароль. Врахуйте що обидва поля можуть бути чутливі до регістру."
        ),
    }

    class Meta:
        model = User
        fields = ('username', 'password')


class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, validators=[])

    def clean(self):
        cleaned_data = self.cleaned_data
        if not User.objects.filter(email=self.cleaned_data['email']).exists():
            self.add_error('email', 'Такого користувача не існує.')
        return cleaned_data


    # class Meta:
    #     model = User
    #     fields = ('email',)


class PasswordResetDoneForm(forms.Form):
    password1 = forms.CharField(max_length=30, min_length=8, required=True)
    password2 = forms.CharField(max_length=30, min_length=8, required=True)

    error_messages = {
        'password_mismatch': _(
            "Паролі не співпадають."
        ),
    }

    class Meta:
        model = User
        fields = ('password1', 'password2')






