from matplotlib.pyplot import flag
from sqlalchemy import false


def resolve():
    N,Y = map(int,input().split())

    flag = True
    ans_list = []
    for i in range(N+1):
        for j in range(N+1):
            k = N - (i+j)
            if k >= 0:
                if 10000*i + 5000*j + 1000*k == Y:
                    ans_list.append([i,j,k])
                    flag = False
                    break
                if flag: continue
    if flag:
        print(-1,-1,-1)
    else:
        print(*ans_list[-1])

    


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
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
