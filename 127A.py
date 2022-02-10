def resolve():
    A,B = map(int,input().split())
    ans = 0

    if A == 0:
        ans = 0
    if A >= 13:
        ans = B
    if 6 <= A  and A <= 12:
        ans = B//2
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
        input = """30 100"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 100"""
        output = """50"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
