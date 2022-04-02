import imp
from itertools import count


def resolve():
    N,Q = map(int,input().split())
    S = input()
    index = [0]*(N+1)
    for i in range(N-1):
        index[i+1] = index[i]+(1 if S[i:i+2] == 'AC' else 0)
    for i in range(Q):
        l,r = map(int,input().split())
        print(index[r-1]-index[l-1])




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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
