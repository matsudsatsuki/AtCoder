from ast import Break
from re import A

from matplotlib.pyplot import flag


def resolve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    dish = [A,B,C,D,E]
    res = [[A%10,A],[B%10,B],[C%10,C],[D%10,D],[E%10,E]]
    res.sort()
    ans = 0
    min = 0  #10で割ったあまり最小を最後にたす
    for r in res:
        if r[0] == 0:
            continue
        else:
            min = r[1]
            break
    flag = True
    for r in res:
        if r[1] == min and flag:
            ans += r[1]
            flag = False
        elif r[1] % 10 == 0:
            ans += r[1]
        else:
            ans += r[1] + (10-r[1]%10)
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
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
