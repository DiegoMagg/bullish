from http import HTTPStatus

import pytest
from accounts.models import User
from django.urls import reverse

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('page', ['login', 'register'])
def test_page_should_be_accessible_by_unauthed_user(page, client):
    response = client.get(reverse(page))
    assert response.status_code == HTTPStatus.OK


def test_user_should_be_able_to_register(client, user_data):
    assert User.objects.filter(email=user_data['email']).exists() is False
    user_data['password_confirmation'] = user_data['password']
    response = client.post(reverse('register'), user_data)
    assert response.status_code == HTTPStatus.FOUND
    assert User.objects.filter(email=user_data['email']).exists() is True


def test_user_should_not_be_able_to_register_if_required_data_is_missing(client, user_data):
    assert User.objects.filter(email=user_data['email']).exists() is False
    user_data['password_confirmation'] = ''
    response = client.post(reverse('register'), user_data)
    assert response.status_code == HTTPStatus.OK
    assert User.objects.filter(email=user_data['email']).exists() is False


def test_user_should_be_able_to_login(client, activated_user, user_data):
    credentials = {'username': user_data['email'], 'password': user_data['password']}
    response = client.post(reverse('login'), credentials)
    assert response.status_code == HTTPStatus.FOUND


def test_login_page_should_redirect_authed_user(authed_client):
    response = authed_client.get(reverse('login'))
    assert response.status_code == HTTPStatus.FOUND
