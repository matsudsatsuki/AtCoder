def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    sm = 0
    x = 0
    for i in range(N):
        sm += abs(x-A[i])
        x = A[i]
    sm += abs(x)
    for i in range(N):
        a = 0
        if i:a = A[i-1]
        b = A[i]
        c = 0
        if i != N-1:c = A[i+1]
        ans = sm
        ans -= abs(a-b)+abs(b-c)
        ans += abs(a-c)
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
        input = """3
3 5 -1"""
        output = """12
8
10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1 1 2 0"""
        output = """4
4
4
2
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
-679 -2409 -3258 3095 -3291 -4462"""
        output = """21630
21630
19932
8924
21630
19288"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
