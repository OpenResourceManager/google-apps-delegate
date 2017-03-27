#! /usr/bin/env python

from __future__ import print_function
import socket
from socketIO_client import SocketIO, LoggingNamespace
from includes.helpers import read_config, read_encrypted_message

IO = None
HOST_NAME = None
BC_KEY = None
DELEGATE_HOST = 'localhost'
DELEGATE_PORT = 3000


def load_config():
    global HOST_NAME, DELEGATE_HOST, DELEGATE_PORT, BC_KEY
    c = read_config()
    HOST_NAME = socket.gethostname()
    DELEGATE_HOST = c['event_server']['host']
    DELEGATE_PORT = c['event_server']['port']
    try:
        if not c['event_server']['bc_key']:
            raise Exception('You have not provided a `bc_key` in your config file! Hint: `php artisan orm:bckey`')
    except KeyError:
        raise KeyError('You have not provided a `bc_key` in your config file! Hint: `php artisan orm:bckey`')
    BC_KEY = c['event_server']['bc_key']


def connect_to_sio():
    global IO
    print('Connecting...')
    IO = SocketIO(DELEGATE_HOST, DELEGATE_PORT, LoggingNamespace)
    print('Connected!')


def main():
    # Load the configuration
    load_config()
    # Connect to the server
    connect_to_sio()
    # Emmit that we're here
    IO.emit('join', {'hostname': HOST_NAME})
    # Hang out
    IO.wait()


if __name__ == "__main__":
    main()
