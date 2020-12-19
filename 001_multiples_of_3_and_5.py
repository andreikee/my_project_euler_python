"""
Multiples of 3 and 5
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
from math import gcd

def lcm(*args):
    if len(args) > 2:
        return lcm(args[0], lcm(*args[1:]))
    a = args[0]
    b = args[1]
    return int(a * b / gcd(a,b))

def sum_of_multiples(limit, multiples=[3, 5]):
    
    res = [x for x in range(1, limit) if any(map(lambda n: x % n == 0, multiples))]
    return sum(res)

def sum_of_multiples_2(limit, multiples=[3, 5, 4]):
    res = 0
    lcm_all = lcm(*multiples)
    for a in multiples:
        s = _sum_multiples(a, limit)
        res += s
        # print(s)
    
    res -= _sum_multiples(lcm_all, limit)
    return res

def _sum_multiples(a, limit):
        lim = limit - 1
        n = lim // a
        m = int(((lim - a) / a) + 1)
        m = a + a * (m - 1)
        s = int((n / 2) * (a + m))
        # print(n, m, s)
        return s


if __name__ == '__main__':
    n = 1000
    multiples = [3, 5]
    print(sum_of_multiples(limit=n, multiples=multiples))

    print(sum_of_multiples_2(limit=n, multiples=multiples))