
from matplotlib.pyplot import flag


def resolve():
    import sympy as sp
    x1,y1,x2,y2 = map(int,input().split())
    sp.init_printing()
    sp.var('x, y')
    eq1=sp.Eq((x-x1)**2+(y-y1)**2,5)
    eq2=sp.Eq((x-x2)**2+(y-y2)**2,5)
    ans = sp.solve ([eq1, eq2],[x,y])

    if int(ans[0][0]) != 0 and int(ans[0][1]) != 0 and int(ans[1][0]) != 0 and int(ans[1][1]) != 0:
        print('Yes')
    else:
        print('No')


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
        input = """0 0 3 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 1 2 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000 999999999 999999999"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
