# Данилович Юстин, 5-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER,
                         json=body)


response = post_new_order(data.order_body)


def get_new_order_track(response):
    return response.json()["track"]


track = get_new_order_track(response)


def get_order_info():
    return requests.get(configuration.URL + configuration.TRACK_ORDER + "track")


info = get_order_info()
