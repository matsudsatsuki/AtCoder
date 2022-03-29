from math import factorial


def resolve():
    from math import factorial
    N,M = map(int,input().split())
    mod = 10**9+7
    if abs(N-M) > 1:
        print(0)
    elif abs(N-M) == 1:
        print((factorial(N)*factorial(M))%mod)
    elif N == M:
        print((2*(factorial(N)*factorial(M)))%mod)








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
        input = """2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000 100000"""
        output = """530123477"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
