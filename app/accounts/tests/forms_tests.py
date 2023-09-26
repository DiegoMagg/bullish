import pytest
from accounts.forms import RegisterForm
from accounts.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('key', ['email', 'name', 'password', 'password_confirmation'])
def test_register_form_should_raise_error_if_field_is_missing(key, registration_form_data):
    registration_form_data[key] = None
    form = RegisterForm(registration_form_data)
    assert form.is_valid() is False
    field_error = form.errors.get(key)
    assert field_error is not None


def test_register_form_should_raise_error_if_email_is_invalid(registration_form_data):
    expected_errors = {'email': ['Enter a valid email address.']}
    registration_form_data['email'] = 'invalid'
    form = RegisterForm(registration_form_data)
    assert form.is_valid() is False
    assert form.errors == expected_errors


def test_register_form_should_raise_error_if_passwords_mismatch(user_data):
    expected_errors = {'password': ['Passwords didn\'t match']}
    user_data['password_confirmation'] = user_data['password'][:-1]
    form = RegisterForm(user_data)
    assert form.is_valid() is False
    assert form.errors == expected_errors


def test_register_form_should_raise_error_if_email_is_already_registered(
    registration_form_data,
    activated_user,
):
    expected_error = {'email': ['This email address is already being used.']}
    form = RegisterForm(registration_form_data)
    assert form.is_valid() is False
    assert form.errors == expected_error


def test_register_form_should_be_valid(registration_form_data):
    form = RegisterForm(registration_form_data)
    assert form.is_valid() is True


def test_register_form_should_create_user(registration_form_data):
    assert User.objects.exists() is False
    form = RegisterForm(registration_form_data)
    assert form.is_valid() is True
    user = form.save()
    user.check_password(form.cleaned_data['password'])
    assert User.objects.exists() is True
