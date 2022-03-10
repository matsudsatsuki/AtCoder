def resolve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    E_x = [0]
    a = 0
    for i in range(N):
        a += (p[i]+1)/2
        E_x.append(a)
    inf = -1e9
    ans = inf
    for i in range(K,N+1):
        s = E_x[i]-E_x[i-K]
        ans = max(ans,s)
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
        input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()