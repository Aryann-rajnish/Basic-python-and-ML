import socketio

import json, requests, pprint, socket, time

#importing libraries
def getToken():
    #url = 'http://103.69.169.10:10521/interactive/user/session'
    url = 'http://103.69.169.10:10521/marketdata/auth/login'

    try:
        headers = {
            'Content-type': 'application/json'
        }

        payload = {
            "userID": "VIREN1",
            "password": "Abcd@1234",
            "publicKey": "9bc8778fd3832848",
            "source": "WebApi"
        }

        response = requests.post(url, data = json.dumps(payload).encode(), headers = headers)

        res = response.json()

        #print('Token Response::', res)

        return res['result']['token']
    except Exception as error:
        print('Token Error:: URL: {} Error: {}'.format(url, error))


def quotes():
    token = getToken()
    #token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiJWSVJFTjEiLCJpYXQiOjE1NTYyNjQ3NjIsImV4cCI6MTU1NjM1MTE2Mn0.WLHQxviMR11YKQoS9gYJoFJjnXs-I0GhPRbBu09jfH4'
    url = 'http://103.69.169.10:10521/marketdata/instruments/quotes'

    if token:
        print('Token::', token)

        try:
            headers = {
                'authorization': token,
                'Content-type': 'application/json'
            }

            payload = {
                "userID": "VIREN1",
                "source": "WebApi",
                "clientID": "VIREN1",
                "instruments": [{
                    "exchangeSegment": 1,
                    "exchangeInstrumentID": 11536
                }],
                "marketDataPort": "1502",
                "publishFormat": "JSON"
            }

            response = requests.post(url, data = json.dumps(payload).encode(), headers = headers)

            pprint.pprint(json.dumps(response.json()))
        except Exception as error:
            print('Process Error:: URL: {} Error: {}'.format(url, error))


def subscriber():
    token = getToken()
    #token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOiJWSVJFTjEiLCJpYXQiOjE1NTYyNjQ3NjIsImV4cCI6MTU1NjM1MTE2Mn0.WLHQxviMR11YKQoS9gYJoFJjnXs-I0GhPRbBu09jfH4'
    url = 'http://103.69.169.10:10521/marketdata/instruments/subscription'
    if token:
        print('Token::', token)

        try:
            headers = {
                'authorization': token,
                'Content-type': 'application/json'
            }

            payload = {
                "userID": "VIREN1",
                "source": "WebApi",
                "clientID": "VIREN1",
                "instruments": [{
                    "exchangeSegment": 1,
                    "exchangeInstrumentID": 11536
                }],
                "marketDataPort": "1502",
            }

            response = requests.post(url, data = json.dumps(payload).encode(), headers = headers)

            pprint.pprint(json.dumps(response.json()))
        except Exception as error:
            print('Process Error:: URL: {} Error: {}'.format(url, error))



#function code to get token of market data
# standard Python
sio = socketio.Client()
@sio.on('connect')
def on_connect():
   #quotes()
   print('I\'m connected!')

@sio.on('message')
def on_message(data):
   print('I received a message!')

@sio.on('1501-json-full')
def on_message(data):
   print('I received a 1501 message!'+data)

@sio.on('1502-json-full')
def on_message(data):
   print('I received a 1502 message!'+data)


@sio.on('1503-json-partial')
def on_message(data):
   print('I received a 1503 message!'+data)

@sio.on('1504-json-full')
def on_message(data):
   print('I received a 1504 message!'+data)

@sio.on('1510-json-partial')
def on_message(data):
   print('I received a 1510 message!'+data)

@sio.on('disconnect')
def on_disconnect():
   print('I\'m disconnected!')


sio.connect('http://103.69.169.10:10521/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJWSVJFTjEiLCJwdWJsaWNLZXkiOiI5YmM4Nzc4ZmQzODMyODQ4IiwiaWF0IjoxNTU4NjA5OTI2LCJleHAiOjE1NTg2OTYzMjZ9.nevg1YGDm0MngpTV-5anomqxaaGBGUdK408H96MGHJM&userID=VIREN1&publishFormat=JSON&broadcastMode=Full',headers={}, transports='websocket', namespaces=None, socketio_path='/marketdata/socket.io')
print("hello")

#subscriber()
sio.wait()


# Add the above code as task and call disconnect when socket need to be closed.
#sio.disconnect()
