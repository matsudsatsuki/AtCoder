from itertools import count


def resolve():
    S = input()
    char_list = []
    count = 0
    for s in S:
        if s in char_list:
            count += 1
            char_list.append(s)
        else:
            char_list.append(s)
    if count == 2:
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
        input = """ASSA"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """STOP"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """FFEE"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """FREE"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
