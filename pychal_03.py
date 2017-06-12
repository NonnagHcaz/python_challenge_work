import os
import re

try:
    from . import requests_helper as rh
except Exception:
    import requests_helper as rh

HERE = 'http://www.pythonchallenge.com/pc/def/equality.html'
URL_BASE = os.path.split(HERE)[0]
URL_EXT = '.php'


def main():
    print('Solving Python Challenge {}:\n\t{}'.format(
        os.path.splitext(__file__)[0][-2:], HERE))
    answer = ''
    base_url = ''

    pattern = r'(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])'
    infile = r'./pychal_q03.txt'
    outfile = r'./pychal_a03.txt'
    with open(infile, 'rb') as in_fp, open(outfile, 'w') as out_fp:

        answer = ''.join(
            re.findall(pattern, ''.join(
                [line.decode("utf-8") for line in in_fp.readlines()])))
        base_url = os.path.join(URL_BASE, answer + URL_EXT)
        out_fp.write(base_url)

    print('Answer: ' + answer)
    rh.open(base_url)


if __name__ == '__main__':
    main()
