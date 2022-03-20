from tkinter.tix import Tree
from matplotlib.pyplot import flag


def resolve():
    import collections
    S = input()
    a = dict(collections.Counter(S))
    flag = True
    for n in a.values():
        if n != 1:
            flag = False
            break
    print('yes'if flag else 'no')




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
        input = """uncopyrightable"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """different"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """no"""
        output = """yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
