from itertools import combinations, count
from math import factorial


def resolve():
    import itertools
    import math
    N,M,K = map(int,input().split())
    mod = 998244353
    n = []
    count = 0
    
    for i in range(1,M+1):
        n.append(i)
    
    


    






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
        input = """2 3 4"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """31 41 592"""
        output = """798416518"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
