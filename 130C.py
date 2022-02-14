def resolve():
    W,H,x,y = map(int,input().split())
    
    def cut_row(W,H,x,y):
        area_r = (W-x)*H
        area_l = x*H
        return min(area_r,area_l)

    def cut_column(W,H,x,y):
        area_d = W*(H-y)
        area_u = W*y
        return min(area_d,area_u)

    A = cut_row(W,H,x,y)
    B = cut_column(W,H,x,y)
    if A == B:
        print(A,1)
    elif A < B:
        print(A,0)
    else:
        print(B,0)
    #answer
    W,H,x,y = map(int,input().split())
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)








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
        input = """2 3 1 2"""
        output = """3.000000 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 1 1"""
        output = """2.000000 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
