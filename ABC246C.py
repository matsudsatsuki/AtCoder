from heapq import heapify
import imp
from sympy import primefactors


def resolve():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    while K:
        a = A.pop()
        a = max(a-X,0)
        K -= 1
        while True:
            if max(A) < a:
                K -= 1
                a = max(a-X,0)
            else:
                break
    ans = 0
    for a in A:
        ans += a
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
        input = """5 4 7
8 3 10 5 13"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 100 7
8 3 10 5 13"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 815 60
2066 3193 2325 4030 3725 1669 1969 763 1653 159 5311 5341 4671 2374 4513 285 810 742 2981 202"""
        output = """112"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
