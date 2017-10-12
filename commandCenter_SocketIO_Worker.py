from socketIO_client import SocketIO, BaseNamespace
from missionControlAPI import missionControlAPI

import json
import random
import uuid
import threading

host = 'localhost'
port = 8000
missionControlAPI = missionControlAPI()

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def server_details(*args):
    socketIO.emit('server_details',missionControlAPI.getServerDetails())

#Define the socketIO connection
socketIO = SocketIO(host, port)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)
socketIO.on('server_details', server_details)


