def resolve():
    N,K,S = map(int,input().split())
    ans = [S]*N
    for i in range(N):
        if S < 1000000000:
            if i > K-1:
                ans[i] = S+1
        elif i > K-1:
            ans[i] = 1
    print(*ans)









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
        input = """4 2 3"""
        output = """1 2 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3 100"""
        output = """50 50 50 30 70"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
