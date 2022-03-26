def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(2001):
        if i not in A:
            print(i)
            break









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
        input = """8
0 3 2 6 2 1 0 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2000 2000 2000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
