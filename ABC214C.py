def resolve():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    if N == 1:
        print(T[0])
        exit()
    inf = float('inf')
    p = [inf]*N
    p[0] = T[0]
    for i in range(1,N):
        p[i] = min(S[i-1]+p[i-1],T[i])
    for a in p:
        print(a)
    






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
        input = """3
4 1 5
3 10 100"""
        output = """3
7
8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
100 100 100 100
1 1 1 1"""
        output = """1
1
1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4
1 2 4 7"""
        output = """1
2
4
7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
84 87 78 16 94 36 87 93
50 22 63 28 91 60 64 27"""
        output = """50
22
63
28
44
60
64
27"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
