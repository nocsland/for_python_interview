Что такое addfinalizer и для чего используется?

addfinalizer - один из элементов фикстуры, предназначен для выполнения завершающего кода при использовании объекта
request-context

import smtplib

import pytest


@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection  # возвращает значение фикстуры
