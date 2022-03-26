from doctest import FAIL_FAST
from itertools import count
from matplotlib.pyplot import flag


def resolve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    flag = True
    dp = [True]*N  
    i = 0 
    inf = 1e10
    past = [A[0],B[0]]
    



            

            
    print('Yes' if flag else 'No')











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
        input = """5 4
9 8 3 7 2
1 6 2 9 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 90
1 1 1 100
1 2 3 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1000000000
1 1 1000000000 1000000000
1 1000000000 1 1000000000"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
