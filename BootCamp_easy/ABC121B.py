def resolve():
    N,M,C = map(int,input().split())
    B = [int(x)for x in input().split()]
    ans = 0
    for i in range(N):
        A = [int(x)for x in input().split()]
        sum = 0
        for j in range(M):
            sum += A[j]*B[j]
        if sum > -C:
            ans += 1
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
        input = """2 3 -10
1 2 3
3 2 1
1 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 -4
-2 5
100 41
100 40
-3 0
-6 -2
18 -13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
