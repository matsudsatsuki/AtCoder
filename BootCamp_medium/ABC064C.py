from itertools import count
from turtle import color
from importlib_metadata import re
from sympy import principal_branch


def resolve():
    N = int(input())
    A = [int(x)for x in input().split()]
    def rank_checker(rate):
        if 1 <= rate <= 399:
            return 'Glay'
        if 400 <= rate <= 799:
            return 'Blown'
        if 800 <= rate <= 1199:
            return 'Green'
        if 1200 <= rate <= 1599:
            return 'Water'
        if 1600 <= rate <= 1999:
            return 'Blue'
        if 2000 <= rate <= 2399:
            return 'Yellow'
        if 2400 <= rate <= 2799:
            return 'Orange'
        if 2800 <= rate <= 3199:
            return 'Red'
        else:
            return 'Others'
    check = set()
    color = ''
    count = 0
    ans = 0
    for rates in A:
        color = rank_checker(rates)
        if color == 'Others':
            count += 1
            continue
        if color in check:continue
        check.add(color)
        ans += 1
    max_ans = ans + count
    if ans == 0:
        min_ans = 1
    else:
        min_ans = ans
    print(min_ans,max_ans)
    #print(ans)









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
        input = """4
2100 2500 2700 2700"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1100 1900 2800 3200 3200"""
        output = """3 5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990"""
        output = """1 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
