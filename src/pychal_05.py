import os
import pickle

try:
    from . import requests_helper as rh
except:
    import requests_helper as rh

HERE = 'http://www.pythonchallenge.com/pc/def/peak.html'
URL_BASE = os.path.split(HERE)[0]
URL_EXT = '.html'


def main():
    print('Solving Python Challenge {}:\n\t{}'.format(
        os.path.splitext(__file__)[0][-2:], HERE))
    answer = ''
    base_url = ''

    infile = r'./dat/pychal_q05.p'
    outfile = r'./out/pychal_a05.txt'
    with open(infile, 'rb') as in_fp, open(outfile, 'w+') as out_fp:
        data = pickle.load(in_fp)
        for line in data:
            out_fp.write(''.join([k * v for k, v in line]) + '\n')

    answer = 'channel'
    base_url = ''
    print('\nAnswer: ' + answer)
    # rh.open(base_url)


if __name__ == '__main__':
    main()
