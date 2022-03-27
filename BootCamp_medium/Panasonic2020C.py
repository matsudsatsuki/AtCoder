from cmath import sqrt
import imp


def resolve():
    a,b,c = map(int,input().split())
    d = c-a-b
    if 4*a*b < d**2 and d > 0:
        print('Yes')
    else:
        print('No')








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
        input = """2 3 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
