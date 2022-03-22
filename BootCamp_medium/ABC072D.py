from aem import con
from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    P = list(map(int,input().split()))
    A = sorted(P)
    flag = False
    ans = 0
    for a,b in zip(P,A):
        if flag:
            flag = False
            continue
        if a == b:
            flag = True
            ans += 1
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
        input = """5
1 4 3 5 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9
1 2 4 9 5 8 7 3 6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
