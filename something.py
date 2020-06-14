import requests
import os
import sys
def ping_google():
    resp = requests.get('https://www.google.com')
    return resp.status_code, resp.text


