from doctest import FAIL_FAST
from math import factorial
from matplotlib.pyplot import flag
from sqlalchemy import false


def resolve():
    N,A,B,C,D = map(int,input().split())
    S = input()
    flag = True
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    if '##' in S[A:C+1] or '##' in S[B:D+1]:
        flag = False
    else:
        if C < D:
            flag = True
        else:
            if '...' in S[B-1:D+2]:
                flag = True
            else:
                flag = False 
    print('Yes' if flag else 'No')


            






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
        input = """7 1 3 6 7
.#..#.."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1 3 7 6
.#..#.."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 1 3 15 13
...#.#...#.#..."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
