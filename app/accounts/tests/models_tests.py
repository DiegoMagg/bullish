import pytest
from accounts.models import User

pytestmark = pytest.mark.django_db


def test_accounts_model_must_create_an_inactive_common_user(user_data):
    assert User.objects.filter(email=user_data['email']).exists() is False
    User.objects.create(**user_data)
    user = User.objects.filter(email=user_data['email'])
    assert user.exists() is True
    assert user.first().is_staff is False
    assert user.first().is_superuser is False
    assert user.first().is_active is False


def test_accounts_model_must_create_a_superuser(user_data):
    assert User.objects.filter(email=user_data['email']).exists() is False
    User.objects.create_superuser(**user_data)
    user = User.objects.filter(email=user_data['email'])
    assert user.exists() is True
    assert user.first().is_staff is True
    assert user.first().is_superuser is True
    assert user.first().is_active is True


def test_user_instance_must_return_user_name(user_data):
    user = User.objects.create(**user_data)
    assert user.__str__() == user_data['name']
