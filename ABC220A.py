from doctest import FAIL_FAST
from re import I

from matplotlib.pyplot import flag


def resolve():
    A,B,C = map(int,input().split())
    i = 1
    flag = False
    while True:
        if A <= C <= B:
            flag = True
            ans = C
            break
        if B < C:
            break
        C *= i
        i += 1
    print(ans if flag else -1)







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
        input = """123 456 100"""
        output = """200"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """630 940 314"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
