from itertools import count


from sympy import re

def resolve():
    import math
    A,B,C,D = map(int,input().split())
    #num_list = [int(i) for i in range(A,B+1)]
    #print(num_list)
    n_sum = B - A + 1
    def return_range(bottom,upper,n):
        #range(low)
        if bottom % n == 0:
            b_range = bottom // n
        else:
            b_range = (bottom // n) + 1
        u_range = upper // n
        c = (u_range - b_range)+1
        return c
    def my_lcm(x, y):
        return (x * y) // math.gcd(x, y)

    a = return_range(A,B,C)
    b = return_range(A,B,D)
    lcm = my_lcm(C,D)
    c = return_range(A,B,lcm)
    ans = n_sum - ((a+b)-c)


    print(ans)

    

    

    









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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
