# Данилович Юстин, 5-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data


def test_get_new_order():
    track = str(requests.post(configuration.URL + configuration.CREATE_ORDER, json=data.order_body).json().get("track"))
    order = requests.get(configuration.URL + configuration.TRACK_ORDER + track)
    status_code = 200
    assert status_code == order.status_code


# В предыдущем коде я создал слишком много функции и переменных. Понял что их можно сократить.
# Начал следовать комментариям в ревью, и у меня получился код ниже. Я решил его оставить чтоб был ясен ход моих мыслей.
# После того как я написал код ниже, я решил сократить его и у меня получился такой автотест.

# def get_new_order_track():
#     return requests.post(configuration.URL + configuration.CREATE_ORDER, json=data.order_body).json().get("track")
#
#
# def test_get_new_order():
#     track = str(get_new_order_track())
#     order = requests.get(configuration.URL + configuration.TRACK_ORDER + track).status_code
#     status_code = 200
#     assert status_code == order
