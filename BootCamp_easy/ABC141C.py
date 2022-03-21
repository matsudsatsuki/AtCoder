from importlib_metadata import collections


def resolve():
    import collections
    N,K,Q = map(int,input().split())
    A = []
    for _ in range(Q):
        a = int(input())
        A.append(a)
    P = [K-Q]*N
    A = dict(collections.Counter(A))
    for a,b in A.items():
        #print(a,b)
        P[a-1] += b
    for p in P:
        if p <= 0:
            print('No')
        else:
            print('Yes')









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
        input = """6 3 4
3
1
3
2"""
        output = """No
No
Yes
No
No
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5 4
3
1
3
2"""
        output = """Yes
Yes
Yes
Yes
Yes
Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9"""
        output = """No
No
No
No
Yes
No
No
No
Yes
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
