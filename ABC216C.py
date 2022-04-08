

from itertools import count


def resolve():
    N = int(input())
    if N == 1:
        print('A')
    elif N == 2:
        print('AA')
    else:
        S = 'AA'
        N -= 2
        count = 1
        while N > 0:
            if N < count*2:
                S += 'B'
                N -= count
                count *= 2
            else:
                S += 'A'*N
    print(S)
            


        





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
        input = """5"""
        output = """AABA"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14"""
        output = """BBABBAAAB"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

