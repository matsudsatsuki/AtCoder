def resolve():
        S = input()
        S = list(S)
        ans = ['0']*4
        for i in range(3):
            if S[i] == '1':
                ans[i+1] = '1'
        print(''.join(ans))
            





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
        input = """1011"""
        output = """0101"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0000"""
        output = """0000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1111"""
        output = """0111"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
