import os
import re

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
    base_url = HERE

    nothing = '12345'

    while True:
        response = rh.post(base_url, {'nothing': nothing})
        if response.status_code is 200:
            content = response.text
            try:
                pattern = r"and the next nothing is (\d+)"
                nothing = re.search(pattern, content).group(1)
            except:
                pattern = r"([a-zA-Z0-9]+.html)"
                try:
                    answer = re.search(pattern, content).group(1)
                    break
                except:
                    nothing = str(int(nothing) // 2)

    base_url = os.path.join(URL_BASE, answer)

    outfile = r'./out/pychal_a04.txt'
    with open(outfile, 'w') as out_fp:
        out_fp.write(base_url)

    print('\nAnswer: ' + answer)
    rh.open(base_url)


if __name__ == '__main__':
    main()
