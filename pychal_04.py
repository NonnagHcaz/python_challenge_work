import os

try:
    from . import requests_helper as rh
except Exception:
    import requests_helper as rh

HERE = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
URL_BASE = os.path.split(HERE)[0]
URL_EXT = '.html'


def main():
    print('Solving Python Challenge {}:\n\t{}'.format(
        os.path.splitext(__file__)[0][-2:], HERE))
    answer = ''
    base_url = ''

    print('Answer: ' + answer)
    rh.open(base_url)


if __name__ == '__main__':
    main()
