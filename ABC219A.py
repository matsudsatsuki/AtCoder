def resolve():
    X = int(input())
    if X < 40:
        print(40-X)
    if 40 <= X < 70:
        print(70-X)
    if 70 <= X < 90:
        print(90-X)
    if X >= 90:
        print('expert')






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
        input = """56"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """32"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100"""
        output = """expert"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
