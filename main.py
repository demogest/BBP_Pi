import time
from concurrent.futures.process import ProcessPoolExecutor
from decimal import Decimal, getcontext
from tqdm import tqdm
import os
import subprocess


def getPow(a, _n):
    res = 1
    while _n:
        if _n & 1:
            res *= a
        _n >>= 1
        a *= a
    return res


def getPi(_n):
    result = (Decimal(4) / Decimal(8 * _n + 1) - Decimal(2) / Decimal(8 * _n + 4) - Decimal(1) / Decimal(
        8 * _n + 5) - Decimal(1) / Decimal(8 * _n + 6)) / Decimal(getPow(16, _n))
    return result


if __name__ == '__main__':
    n = input()
    start = time.time()
    params = list(tqdm([i for i in range(int(n))], desc="Creating params list"))
    # noinspection SpellCheckingInspection
    getcontext().prec = int(n)
    pool = ProcessPoolExecutor(max_workers=16)
    print("start")
    results = list(tqdm(pool.map(getPi, params), total=len(params), desc='Calculating pi with bbp：'))

    end = time.time()
    print("use %fs" % (end - start))
    pi = Decimal(0)
    for r in results:
        pi += r
    # print(pi)
    with open('pi.txt', 'w') as f:
        f.write(str(pi))
    print('saving to pi.txt({}B)'.format(os.stat('pi.txt').st_size))
    com = input('Open file?([y]/n):')
    if com == 'y' or com == '':
        subprocess.Popen([r'C:\Program Files\Sublime Text\sublime_text.exe', r'./pi.txt'])
        exit(0)
    else:
        exit(0)
