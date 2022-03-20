from matplotlib.pyplot import flag


def resolve():
    S = input().split()
    T = input().split()
    flag = True
    if S == T or (S[0] != T[0] and S[1] != T[1] and S[2] != T[2]):
        flag = True
    else:
        flag = False
    print('Yes' if flag else 'No')







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
        input = """R G B
R G B"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
