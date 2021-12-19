import websocket
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.environ.get('API_KEY')


def getWSApiKey():
    url = "https://api3.loopring.io/v3/ws/key"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': apiKey
    }

    return requests.request("GET", url, headers=headers).json()['key']


root = 'wss://ws.api3.loopring.io/v3/ws'
wsApiKey = '?wsApiKey=' + getWSApiKey()
wsUrl = f'{root}{wsApiKey}'


def on_message(wsapp, message):

    if message == 'ping':
        ws.send('pong')
    else:
        print(datetime.now())
        print(message)
        print('\n')


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    subscriptions = {
        "op": "sub",
        "unsubscribeAll": False,
        "topics": [
            {
                "topic": "candlestick",
                "market": "LRC-USDC",
                "interval": "15min"
            },
            {
                "topic": "candlestick",
                "market": "LRC-ETH",
                "interval": "1min"
            }
        ]
    }
    ws.send(json.dumps(subscriptions))
    print("Opened connection")


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(wsUrl,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
