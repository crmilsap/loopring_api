import websocket
import requests
import json
from datetime import datetime


apiKey = '5A6IeTqEh0kUURlDJXO0De3O6buEQfkxoNPHa6Lirdoo6Tk7CQwxiBsG9y5gWM2U'


def getWSApiKey():
    url = "https://api3.loopring.io/v3/ws/key"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': apiKey
    }

    return requests.request("GET", url, headers=headers).json()['key']


def on_message(wsapp, message):
    print('\n')
    print(datetime.now())
    print(message)


# def on_ping(wsapp, message):
#     print("Got a ping! A pong reply has already been automatically sent.")


# def on_pong(wsapp, message):
#     print("Got a pong! No need to respond")


websocket.enableTrace(True)
root = 'wss://ws.api3.loopring.io/v3/ws'
wsApiKey = '?wsApiKey=' + getWSApiKey()
wsapp = websocket.WebSocketApp(f'{root}{wsApiKey}',
                               on_message=on_message)
wsapp.run_forever(ping_interval=30, ping_timeout=10)
