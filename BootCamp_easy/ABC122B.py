from itertools import count
from matplotlib.pyplot import flag


def resolve():
    S = input()
    ans_lis = [0]*len(S)
    count = 0
    for i in range(len(S)):
        if (S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T'):
            count += 1
            ans_lis[i] = count
        else:
            count = 0
    print(max(ans_lis))





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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """HATAGAYA"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """SHINJUKU"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
