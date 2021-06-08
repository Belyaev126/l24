#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 6

import math
from threading import Thread


def sm_first(x, n):
    return ((-1) ** (n - 1)) * x / n


def first(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_first(x, n)
    n += 1
    test = math.log(x + 1)

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm_first(x, n)
        n += 1
        print(n)

    current = round(current, 2)
    test = round(test, 2)
    print(f'Сумма ряда {current} ~ проверочному значению {test}')


if __name__ == '__main__':
    th1 = Thread(target=first(math.pi / 3, 1))

    th1.start()
