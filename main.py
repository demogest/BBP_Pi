import time
from concurrent.futures.process import ProcessPoolExecutor
from decimal import Decimal, getcontext
from tqdm import tqdm

def getPow(a, n):
    res = 1
    while n:
        if n & 1:
            res *= a
        n >>= 1
        a *= a
    return res


def getPi(n):
    # 使用BBP公式，n即是π的精度，故精度为22000位
    result = (Decimal(4) / Decimal(8 * n + 1) - Decimal(2) / Decimal(8 * n + 4) - Decimal(1) / Decimal(
        8 * n + 5) - Decimal(1) / Decimal(8 * n + 6)) / Decimal(getPow(16, n))
    return result


if __name__ == '__main__':
    n = input()
    start = time.time()
    params = list(tqdm([i for i in range(int(n))], desc="Creating params list"))
    getcontext().prec = int(n)
    # 进程池，最大工作数设置为4
    pool = ProcessPoolExecutor(max_workers=4)
    print("start")
    results = list(tqdm(pool.map(getPi,params), total=len(params), desc='Calculating pi with bbp：'))

    end = time.time()
    print("use %fs" %(end - start))
    pi = Decimal(0)
    for r in results:
        pi += r
    # print(pi)
    with open('pi.txt', 'w')as f:
        f.write(str(pi))