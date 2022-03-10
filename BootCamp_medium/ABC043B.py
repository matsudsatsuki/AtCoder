def resolve():
    s = input()
    ans_list = []
    for a in s:
        if a == 'B' and ans_list:
            ans_list.pop()
        if a != 'B':
            ans_list.append(a)
    print(''.join(ans_list)) 










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
        input = """01B0"""
        output = """00"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0BB1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
