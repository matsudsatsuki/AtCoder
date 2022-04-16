def resolve():
    from collections import defaultdict
    d = defaultdict(int)
    N = int(input())
    A = list(map(int,input().split()))
    for a in A:
        d[a] += 1
    #print(d)
    Q = int(input())
    for _ in range(Q):
        l,r,x = map(int,input().split())
        if x in A[l-1:r]:
            print(d[x])
        else:
            print(0)
        






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
4
1 5 1
2 4 3
1 5 2
1 3 3"""
        output = """2
0
0
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
