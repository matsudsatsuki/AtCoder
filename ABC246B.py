from cmath import sqrt


def resolve():
    from math import sqrt
    A,B = map(int,input().split())
    C = sqrt(A**2+B**2)
    x = A/C
    y = B/C
    print(x,y)








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
        input = """3 4"""
        output = """0.600000000000 0.800000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 0"""
        output = """1.000000000000 0.000000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """246 402"""
        output = """0.521964870245 0.852966983083"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
