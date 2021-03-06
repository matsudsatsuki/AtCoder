def resolve():
    R,G,B,N = map(int,input().split())
    ans = 0
    R_n = N//R
    G_n = N//G
    B_n = N//B
    #print(R_n,G_n,B_n)
    for i in range(R_n+1):
        for j in range((N-i*R)//G+1):
            if (N-i*R-j*G)%B == 0:
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
        input = """1 2 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 1 4 3000"""
        output = """87058"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
