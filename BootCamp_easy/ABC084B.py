from math import factorial

from aem import con


def resolve():
    A,B = map(int,input().split())
    S = input()
    flag = True
    if len(S) != A+B+1:
        flag = False    
    if S[A] != '-':
        flag = False
    num_lis = [str(i) for i in range(0,10)]
    for i in range(len(S)):
        if i == A:continue
        if S[i] not in num_lis:
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
        input = """3 4
269-6650"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
---"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2
7444"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
