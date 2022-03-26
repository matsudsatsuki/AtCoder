from re import X


def resolve():
    x,y = map(int,input().split())
    dif = abs(abs(x)-abs(y))
    ans = 0
    if abs(x) == abs(y):
        ans = 1
    elif (x > 0 and y < 0) or (x < 0 and y > 0):
        ans = dif+1
    elif x == 0:
        if y >= 0:
            ans = y
        else:
            ans = abs(y)+1
    elif y == 0:
        if x <= 0:
            ans = abs(x)
        else:
            ans = abs(x)+1
    elif x > 0 and y > 0:
        if x <= y:
            ans = y-x
        else:
            ans = x-y+2
    elif x < 0 and y < 0:
        if x <= y:
            ans = abs(y-x)
        else:
            ans = abs(y-x) +2
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
        input = """10 20"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 -10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-10 -20"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
