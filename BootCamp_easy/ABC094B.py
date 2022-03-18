def resolve():
    N,M,X = map(int,input().split())
    A = list(map(int,input().split()))
    dis = [0]*N
    for a in A:
        dis[a] = 1
    #print(dis)
    ans = min(sum(dis[X:]),sum(dis[:X]))
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
        input = """5 3 3
1 2 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3 2
4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 7 5
1 2 3 4 6 8 9"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
