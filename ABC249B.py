from doctest import FAIL_FAST


def resolve():
    S = input()
    #print(ord('A'),ord('Z'))
    A = []
    for i in range(65,91):
        A.append(chr(i))
    a = []
    for j in range(97,123):
        a.append(chr(j))
    flag1 = False
    flag2 = False
    for c in S:
        if c in A:
            flag1 = True
        if c in a:
            flag2 = True
    s = set(list(S))


    print('Yes' if flag1 and flag2 and len(s) == len(S) else 'No')








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
        input = """AtCoder"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """Aa"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """Perfect"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
