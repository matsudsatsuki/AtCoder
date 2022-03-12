import imp


def resolve():
    import math
    N,X = map(int,input().split())
    cities = list(map(int,input().split()))
    diff = []
    for i in range(N):
        diff.append(abs(cities[i]-X))
    ans = diff[0]
    for i in range(1,len(diff)):
        ans = math.gcd(ans,diff[i])
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
        input = """3 3
1 7 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 81
33 105 57"""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
1000000000"""
        output = """999999999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
