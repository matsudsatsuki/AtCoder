from importlib_metadata import itertools
from sympy import primefactors


def resolve():

    N,M = map(int,input().split())
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(M):
        k,*s = list(map(int,input().split()))
        d[i] = s
    P = list(map(int,input().split()))
    from itertools import product
    ans = 0
    for bits in itertools.product([0,1],repeat=N):
        cur = 0
        for k,v in d.items():
            tmp = 0
            for s in v:
                tmp += bits[s-1]
            if P[k] == tmp%2:
                cur += 1
        if cur == M:
            ans += 1
    print(ans)









import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
