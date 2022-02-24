from itertools import count
from zlib import DEF_BUF_SIZE


def resolve():
    N = int(input())
    a = str(N)
    n = len(a)
    #print(n)
    ans = 0
    if n % 2 == 0:
        if n == 2:
            ans = 9
        elif n >= 4:
            ans = 9
            for i in range(2,n,2):
                ans += (10**(i))*9
    if n % 2 != 0:
        if n % 2 == 1:
            ans += N % (10**(n-1)) + 1
            ans += 9
        else:
            ans += N % (10**n)
            ans += 9 + (10**(n-2))*9
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
        input = """11"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """136"""
        output = """46"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000"""
        output = """90909"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
