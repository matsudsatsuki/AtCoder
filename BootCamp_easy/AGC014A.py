


def resolve():
    A,B,C = map(int,input().split())
    ans = 0
    while True:
        if A%2 or B%2 or C%2:
            print(ans)
            break
        elif A == B and B == C:
            print(-1)
            break
        a = (B+C)//2
        b = (A+C)//2
        c = (A+B)//2
        A,B,C = a,b,c
        ans += 1







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
        input = """4 12 20"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 14 14"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """454 414 444"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
