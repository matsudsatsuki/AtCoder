from audioop import reverse


def resolve():
    import math
    N = int(input())
    A = list(map(int,input().split()))
    inf = 1e9
    ans = inf
    for i in range(N-1):
        ans = min(ans,math.gcd(A[i],A[i+1]))
    print(int(ans))






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
2 10 8 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 13 8 1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1000000000 1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
