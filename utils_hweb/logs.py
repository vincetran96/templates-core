'''Logging utils
'''
import time
import traceback
import requests
from pathlib import Path


def write_log(path, mode, msg):
    '''Writes log

    ---
    :params:
    ---
        - path: str - full path (including filename)
        - mode: str - write or append
        - msg: str - message
    '''
    log_path = Path(path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, mode) as logfile:
        logfile.write(msg)

def elapsed_time_closure():
    '''Returns the number of seconds elapsed since the
    last time this function is called
    '''
    last_time = time.monotonic()

    def elapsed_time():
        '''Returns the number of seconds elapsed since the
        function variable is initialized
        '''
        nonlocal last_time
        current_time = time.monotonic()
        elapsed = current_time - last_time
        last_time = current_time
        return elapsed

    return elapsed_time

def get_exc_message():
    '''Returns exception message
    '''
    return traceback.format_exc()

def send_msg_webhook(webhook_url: str, msg: str, **kwargs):
    '''Sends a message to a webhook URL
    '''
    resp = requests.post(url=webhook_url, data=msg, **kwargs)
    resp.raise_for_status()
    return resp.status_code
