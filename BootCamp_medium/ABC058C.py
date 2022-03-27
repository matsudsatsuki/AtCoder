from itertools import count
from importlib_metadata import collections


def resolve():
    N = int(input())
    alpha = ''
    for i in range(ord('a'),ord('z')+1):
        alpha += chr(i)
    S = []
    for _ in range(N):
        S.append(input().strip())
    #print(S)
    for c in alpha:
        min_ = float('inf')
        for s in S:
            count = s.count(c)
            if count < min_:
                min_ = count
        print(c*min_, end='')
    print()

                    
        


        







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
        input = """3
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
