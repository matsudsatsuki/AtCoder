

def resolve():
    import collections
    N = int(input())
    D = list(map(int,input().split()))
    M = int(input())
    T = list(map(int,input().split()))
    flag = True
    a = dict(collections.Counter(D))
    b = dict(collections.Counter(T))
    for i in range(M):
        if T[i] not in a:
            flag = False
            break
        if a[T[i]] < b[T[i]]:
            flag = False
            break
    print('YES'if flag else 'NO')

    



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
        input = """5
3 1 4 1 5
3
5 4 3"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
100 200 500 700 1200 1600 2000
6
100 200 500 700 1600 1600"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
800
5
100 100 100 100 100"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
