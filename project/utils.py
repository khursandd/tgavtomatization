import requests

BOT_TOKEN = '7356746562:AAEAaiLpQiHlNspctg6bmHpzW2fVqLVJf6U'
URL = 'https://api.telegram.org/bot7356746562:AAEAaiLpQiHlNspctg6bmHpzW2fVqLVJf6U/sendMessage'

def send_message(text):
    requests.post(URL, params={
        'chat_id': -1001689034214,
        'text': text})


def send_photo(photo):
    requests.post(
        URL, 
        files={
            'photo': photo,
        },
        params={
            'chat_id': -1001689034214,
        })