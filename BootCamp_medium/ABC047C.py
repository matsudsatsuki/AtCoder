from itertools import count


def resolve():
    S = input()
    count = 0
    for i in range(1,len(S)):
        if S[i-1]+S[i] == 'BW' or S[i-1]+S[i] == 'WB':
            count += 1
    print(count)

        
    





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
        input = """BBBWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """WWWWWW"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """WBWBWBWBWB"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
