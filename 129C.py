
def resolve():
    N,M = map(int,input().split())
    mod = 1e9+7
    stairs = [True]*(N+1)
    for _ in range(M):
        broken = int(input())
        stairs[broken] = False
    dp = [0]*(N+1)
    dp[0] = 1
    for now in range(N):
        for next in range(now+1,min(N+1,now+3)):
            if stairs[next]:
                dp[next] += dp[now]
                dp[next] %= mod
    print(int(dp[N]))



            
    
    


















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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
