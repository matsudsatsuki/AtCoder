from aem import con


def resolve():
    x_1,y_1 = map(int,input().split())
    x_2,y_2 = map(int,input().split())
    x_3,y_3 = map(int,input().split())
    x_4,y_4 = 0,0
    if x_1 == x_2:
        x_4 = x_3
    if x_2 == x_3:
        x_4 = x_1
    if x_1 == x_3:
        x_4 = x_2
    if y_1 == y_2:
        y_4 = y_3
    if y_2 == y_3:
        y_4 = y_1
    if y_1 == y_3:
        y_4 = y_2
    print(x_4,y_4)

    










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
        input = """-1 -1
-1 2
3 2"""
        output = """3 -1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-60 -40
-60 -80
-20 -80"""
        output = """-20 -40"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
