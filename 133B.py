from cmath import sqrt
from itertools import count
from traceback import print_tb


def resolve():
    import math
    N,D = map(int,input().split())
    dis_lis = [list(map(int,input().split()))for i in range(N)]
    a = []
    b = 0
    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            for k in range(D):
                b = (dis_lis[i][k]-dis_lis[j][k])**2
                a.append(b)
            c = sum(a)
            g = math.sqrt(c)
            del a[:]
            if g.is_integer():
                count += 1
    print(count)
            
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
        input = """3 2
1 2
5 5
-2 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1
2
3
4
5"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
