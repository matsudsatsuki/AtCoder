from itertools import count


def resolve():
    N = int(input())
    S = input()
    count = 0
    ans_lis = [0]
    for i in range(N):
        if S[i] == 'D':
            count -= 1
        if S[i] == 'I':
            count += 1
        ans_lis.append(count)
    print(max(ans_lis))







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
IIDID"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
DDIDDII"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
