import urllib
import webbrowser
import requests

DEFAULT_HEADERS = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}


def open(base_url, params=None):
    payload = _format_payload(params)
    url = '?'.join([base_url, payload])
    webbrowser.open_new(url)


def post(base_url, params=None, headers=None):

    payload = _format_payload(params)

    return requests.get(
        base_url, headers=headers or DEFAULT_HEADERS, data=payload)


def get(base_url, params, headers=None):

    payload = _format_payload(params)

    return requests.get(
        base_url, headers=headers or DEFAULT_HEADERS, data=payload)


def _format_payload(params=None):
    try:
        # Python 3
        payload = urllib.parse.urlencode(params)
    except AttributeError:
        # Python 2
        payload = urllib.urlencode(params)
    except TypeError:
        # None
        payload = ''

    return payload
