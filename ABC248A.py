def resolve():
    S = input()
    s = ['0','1','2','3','4','5','6','7','8','9']

    for a in s:
        if a not in S:
            print(a)
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
        input = """023456789"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """459230781"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
