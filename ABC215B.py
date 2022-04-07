





from itertools import count
from math import log2

from numpy import mat


def resolve():
    N = int(input())
    count = 1
    for i in range(61):
        if count > N:
            print(i-1)
            break
        else:
            count *= 2

    
    








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
        input = """6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000"""
        output = """59"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
