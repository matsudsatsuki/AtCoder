def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    tw = []
    for a in A:
        if a % 2 == 0:
            count = a / 2
            tw.append(int(count))

    count_2 = 0
    count_4 = 0
    for b in tw:
        if b % 2 != 0:
            count_2 += 1
        else:
            count_4 += 1
    print('Yes'if count_4+(count_2//2) >= N//2 else 'No')











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
        input = """3
1 10 100"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """6
2 7 1 8 2 8"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
