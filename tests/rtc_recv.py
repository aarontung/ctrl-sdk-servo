import time
import signal
import sys
import rtc_sdk
import argparse

RTC_CONNECTION_STATE = [
    'NONE',
    'DISCONNECTED',
    'CONNECTING',
    'CONNECTED',
    'RECONNECTING',
    'FAILED',
]

def parse_args():
    parser = argparse.ArgumentParser(description='Process some command line arguments.')

    parser.add_argument('--secret_id', required=True, help='The secret ID')
    parser.add_argument('--secret_key', required=True, help='The secret key')
    parser.add_argument('--room_id', required=True, help='The ID of the room')

    args = parser.parse_args()

    return args

def signal_handler(sig, frame):
    rtc_sdk.disconnect()
    sys.exit(0)

def on_message_received(msg):
    print('Received message: ', msg)

def on_connection_state_changed(state):
    print('Connection state changed:', RTC_CONNECTION_STATE[state])

if __name__ == '__main__':
    args = parse_args()
    signal.signal(signal.SIGINT, signal_handler)
    rtc_sdk.register_event_callback(on_message_received, on_connection_state_changed)
    rtc_sdk.connect(args.secret_id, args.secret_key, args.room_id)
    while True:
        time.sleep(1)
