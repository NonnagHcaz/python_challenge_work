import os

try:
    from . import requests_helper as rh
except:
    import requests_helper as rh

HERE = 'http://www.pythonchallenge.com/pc/def/274877906944.html'
URL_BASE = os.path.split(HERE)[0]
URL_EXT = '.html'


def main():
    print('Solving Python Challenge {}:\n\t{}'.format(
        os.path.splitext(__file__)[0][-2:], HERE))
    answer = ''
    base_url = ''

    base_url = os.path.join(URL_BASE, answer + URL_EXT)
    print('\nAnswer: ' + answer)
    rh.open(base_url)


if __name__ == '__main__':
    main()
