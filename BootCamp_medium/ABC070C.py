def resolve():
    import math
    N = int(input())
    T = []
    for _ in range(N):
        t = int(input())
        T.append(t)
    def lcm(a,b):
        return a*b // math.gcd(a,b)
    ans = T[0]
    for i in range(1,N):
        ans = lcm(ans,T[i])
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
        input = """2
2
3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2
5
10
1000000000000000000
1000000000000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
