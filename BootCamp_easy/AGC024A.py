from sympy import limit


def resolve():
    A,B,C,K = map(int,input().split())
    if not K % 2:
        print(A-B)
    else:
        print(B-A)




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
        input = """1 2 3 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 2 0"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000 1000000000 1000000000000000000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
