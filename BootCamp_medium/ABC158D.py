
def resolve():
    from collections import deque
    S = input()
    S = deque(S)
    Q = int(input())
    flag = True
    for _ in range(Q):
        a,*b = input().split()
        if a == '1':
            flag = not flag
        
        if a == '2' and flag:
            if b[0] == '1':
                S.appendleft(b[1])
            if b[0] == '2':
                S.append(b[1])
        if a == '2' and not flag:
            if b[0] == '1':
                S.append(b[1])
            if b[0] == '2':
                S.appendleft(b[1])
    A = list(S)
    A = A[::-1]
    print(''.join(S) if flag else ''.join(A))

            






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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
