


def resolve():
    N = int(input())
    n = 998244353
    dp = [[1048576]*10]
    for i in range(1,10):
        dp[1][i] = 1    

    
    for d in range(2,N+1):
        for i in range(1,10):
            for j in range(max(1,i-1),min(9,i-1)+1):
                dp[d][j] += dp[d-1][j]
                dp[d][j] %= n
    res = 0
    #for i in range(1,9):
        #res += dp[N][i]
        #res %= n
    print(dp)
    
    

    





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
        input = """4"""
        output = """203"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """25"""
        self.assertIO(input, output)

    #def test_入力例_3(self):
        #input = """1000000"""
        #output = """248860093"""
        #self.assertIO(input, output)
    def test_入力例_4(self):
        input = """3"""
        output = """69"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()
