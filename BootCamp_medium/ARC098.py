from itertools import product


def resolve():
    N = int(input())
    S = input()
    ans = S[1:].count('E')
    t = ans
    for i in range(1,N):
        if S[i-1] == 'W':
            t += 1
        if S[i] == 'E':
            t -= 1
        ans = min(ans,t)
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
WEEWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
