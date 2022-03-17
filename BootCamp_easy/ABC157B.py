from math import factorial


def resolve():
    A = [list(map(int,input().split()))for _ in range(3)]
    N = int(input())
    B = []
    for _ in range(N):
        b = int(input())
        B.append(b)
    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                A[i][j] = True
            else:
                A[i][j] = False
    flag = False
    for i in range(3):
        if A[i][0] and A[i][1] and A[i][2]: 
            flag = True
        if A[0][i] and A[1][i] and A[2][i]:
            flag = True
    if A[0][0] and A[1][1] and A[2][2]:
        flag = True
    if A[0][2] and A[1][1] and A[2][0]:
        flag = True
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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
