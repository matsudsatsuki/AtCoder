
def resolve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = float('inf')
    ai = bi = 0
    while ai < N and bi < M:
        ans = min(ans,abs(A[ai]-B[bi]))
        if A[ai] < B[bi]:
            ai += 1
        else:
            bi += 1
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
        input = """2 2
1 6
4 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()



