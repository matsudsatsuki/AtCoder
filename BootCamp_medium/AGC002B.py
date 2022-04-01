def resolve():
    N,M = map(int,input().split())
    dp = [False]*N
    ball = [1]*N
    dp[0] = True
    for _ in range(M):
        x,y = map(int,input().split())
        if dp[x-1]:
            if ball[x-1] == 1:
                ball[x-1] -= 1
                ball[y-1] += 1
                dp[x-1] = False
                dp[y-1] = True
            else:
                dp[y-1] = True
                ball[x-1] -= 1
                ball[y-1] += 1
        else:
            ball[x-1] -= 1
            ball[y-1] += 1
            if ball[x-1] == 0:
                dp[x-1] = False
        
    print(dp.count(True))





    











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

    def test_入力例1(self):
        input = """3 2
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

