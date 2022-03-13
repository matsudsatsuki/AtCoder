from tkinter.tix import Tree


def resolve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    d = []
    for i in range(M-1):
        d.append(abs(X[i+1]-X[i]))
    d.sort(reverse=True)
    ans = 0

    print((X[M-1]-X[0])-sum(d[:N-1]) if M-N >= 0 else 0)









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
        input = """2 5
10 12 1 2 14"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 7
-10 -3 0 9 -100 2 17"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1
-100000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
