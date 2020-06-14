import os
import sys

import requests


def ping_google():
    resp = requests.get("https://www.google.com")
    return resp.status_code
