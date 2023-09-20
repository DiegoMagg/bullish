import pytest
from model_bakery import baker


@pytest.fixture
def user_data():
    return {
        'email': 'email@domain.com',
        'name': 'Name Surname',
        'password': '%x3oRGsv7NYTMd',
    }


@pytest.fixture
def registration_form_data(user_data):
    user_data['password_confirmation'] = user_data['password']
    return user_data


@pytest.fixture
def user(user_data):
    user = baker.make('accounts.User', email=user_data['email'], name=user_data['name'])
    user.set_password(user_data['password'])
    return user


@pytest.fixture
def activated_user(user):
    user.is_active = True
    user.save()
    user.refresh_from_db()
    return user
