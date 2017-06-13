import urllib
import webbrowser
import requests

DEFAULT_HEADERS = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}


def open(base_url, params=None, new=0, autoraise=True):
    payload = _format_payload(params)
    if payload:
        url = '?'.join([base_url, payload])
    else:
        url = base_url
    webbrowser.open(url, new, autoraise)


def post(base_url, params=None):

    payload = _format_payload(params)

    return requests.post(
        base_url, params=payload)


def get(base_url, params):

    payload = _format_payload(params)

    return requests.get(
        base_url, data=payload)


def _format_payload(params=None):
    try:
        # Python 3
        payload = urllib.parse.urlencode(params)
    except AttributeError:
        # Python 2
        payload = urllib.urlencode(params)
    except TypeError:
        # None
        payload = None
    return payload
