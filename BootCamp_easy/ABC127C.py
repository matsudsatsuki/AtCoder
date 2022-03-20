from doctest import FAIL_FAST
from itertools import count
from math import factorial
from re import I
from matplotlib.pyplot import flag
from nbformat import read


def resolve():
    N,M = map(int,input().split())
    L,R = [],[]
    for _ in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    ans = min(R)-max(L)+1
    print(ans if max(L) <= min(R) else 0)



    


        
    













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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
