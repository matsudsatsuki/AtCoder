from ast import Break


def resolve():
    X = int(input())
    ans = X // 10
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
        input = """47"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-24"""
        output = """-3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """50"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """-30"""
        output = """-3"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """987654321987654321"""
        output = """98765432198765432"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
