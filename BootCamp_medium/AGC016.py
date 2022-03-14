from itertools import count
from tkinter.tix import Tree


def resolve():
    s = list(map(ord,list(input())))
    a = ord('a')
    z = ord('z')
    min_a = len(s)
    for c in range(a,z+1):
        max_a = -1
        count = 0
        for si in s:
            if si == c:
                max_a = max(max_a,count)
                count = 0
            else:
                count += 1
        max_a = max(max_a,count)
        min_a = min(min_a,max_a)
    print(min_a)
    #for g in range(a,z+1):
        #print(chr(g))
        #a,b,c,d....

    










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
        input = """serval"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """jackal"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """zzz"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """whbrjpjyhsrywlqjxdbrbaomnw"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
