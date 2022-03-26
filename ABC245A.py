def resolve():
    A,B,C,D = map(int,input().split())
    if A < C:
        print('Takahashi')
    elif A > C:
        print('Aoki')
    elif A == C:
        if B < D:
            print('Takahashi')
        elif B == D:
            print('Takahashi')
        elif B > D:
            print('Aoki')

        









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
        input = """7 0 6 30"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 30 7 30"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 0 23 59"""
        output = """Takahashi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
