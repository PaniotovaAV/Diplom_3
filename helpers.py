import requests
from faker import Faker

fake = Faker(locale="ru_RU")


def email_():
    return fake.email()


def password_():
    return fake.password(length=10)


def first_name_():
    return fake.first_name()


def register_new_user_and_return_login_password():
    login_pass = []
    email = email_()
    password = password_()
    name = first_name_()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    response.json()
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
    return login_pass
