def resolve():
    N,L = map(int,input().split())
    K = int(input())
    A = [0]+list(map(int,input().split()))
    A.append(L)
    def check(x):
        cnt = 0
        l = 0
        for i in range(N+1):
            l += A[i+1]-A[i]
            if l >= x:
                cnt += 1
                l = 0
        return cnt >= K+1
    left = L
    right = -1
    while left - right > 1:
        mid = (left+right)//2
        if check(mid):
            right = mid
        else:
            left = mid
    print(left-1)

    
    







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
        input = """3 34
1
8 13 26"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 45
2
7 11 16 20 28 34 38"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 100
1
28 54 81"""
        output = """46"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 100
2
28 54 81"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954"""
        output = """170"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
