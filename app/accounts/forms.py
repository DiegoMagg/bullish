from accounts.models import User
from django import forms
from django.contrib.auth import authenticate, password_validation
from django.utils.translation import gettext as _


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
        strip=True,
        validators=[password_validation.validate_password],
    )
    password_confirmation = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput,
        strip=True,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('This email address is already being used.'))
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.data.get('password_confirmation')
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError(_('Passwords didn\'t match'))
        return password

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        instance.set_password(instance.password)
        instance.is_active = True
        instance.save() if commit else None
        return instance

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'password',
            'password_confirmation',
        ]
