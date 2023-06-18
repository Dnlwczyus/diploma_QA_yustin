# Данилович Юстин, 5-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import requests
import configuration
import sender_stand_request


def assert_code(status_code_expected):
    assert status_code_expected == sender_stand_request.info.status_code

def test_code():
    assert_code(200)

