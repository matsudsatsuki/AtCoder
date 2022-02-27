from distutils.filelist import findall
from itertools import count

from cmd2 import ansi
from matplotlib.pyplot import flag


def resolve():
    S = input()
    nums = [0 for _ in range(len(S)+1)]
    for i in range(len(S)):
        if S[i] == '<':
            nums[i+1] = max(nums[i]+1,nums[i+1])
    for j in range(-1,-len(S),-1):
        if S[j] == '>':
            nums[j-1] = max(nums[j-1],nums[j]+1)
    print(sum(nums))
    


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
        input = """<>>"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """<>>><<><<<<<>>><"""
        output = """28"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
