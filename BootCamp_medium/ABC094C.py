from statistics import median


def resolve():
    N = int(input())
    X = list(map(int,input().split()))
    A = sorted(X)
    for i in range(N):
        if X[i] <= A[(N//2)-1]:
            print(A[N//2])
        else:
            print(A[(N//2)-1])













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
        input = """4
2 4 4 3"""
        output = """4
3
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 2"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
5 5 4 4 3 3"""
        output = """4
4
4
4
4
4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
