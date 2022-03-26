def resolve():
    N,M = int(input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    







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
        input = """1 2
2 1
12 14 8 2"""
        output = """6 4 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
100 1
10000 0 -1"""
        output = """100 -1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
