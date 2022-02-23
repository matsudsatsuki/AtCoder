from ast import Num
from itertools import count
from operator import xor

from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    n_list = [int(x)for x in input().split()]
    sort_list = sorted(n_list)
    count = 0
    for a,b in zip(n_list,sort_list):
        if a != b:
            count += 1
        else:
            continue
    if count > 2:
        print('NO')
    else:
        print('YES')


    








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
5 2 3 4 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 4 3 5 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6 7"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
