def resolve():
    N = int(input())
    S = input()
    print(S[-1])







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
        input = """5
abcde"""
        output = """e"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
a"""
        output = """a"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
