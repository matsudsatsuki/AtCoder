from matplotlib.pyplot import flag


def resolve():
    A,B,C,X = map(int,input().split())
    N = 1000-A
    ans = 0
    flag = True
    if X <= A:
        ans = 1.000000000
        flag = False
    if X > B and flag:
        ans = 0.0000000
        flag = False

    if flag:
        ans = C/(B-A)
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
        input = """30 500 20 103"""
        output = """0.042553191489"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """50 500 100 1"""
        output = """1.000000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2 1 1000"""
        output = """0.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

