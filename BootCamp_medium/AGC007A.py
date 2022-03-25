from doctest import FAIL_FAST


def resolve():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    double = 0
    flag = True
    for y in range(H):
        for x in range(W):
            double = 0
            above = 0
            if S[y][x] == '#':
                if x < W-1:
                    if S[y][x+1] == '#':
                        double += 1
                if y < H-1:
                    if S[y+1][x] == '#':
                        double += 1
                if x > 0 and S[y][x-1] == '#':
                    above += 1
                if y > 0 and S[y-1][x] == '#':
                    above += 1
                if (double != 1 and y+x != H+W-2) or (above == 0 and y+x != 0):
                    flag = False
                    break
    print('Possible' if flag else 'Impossible')
                    



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
        input = """4 5
##...
.##..
..##.
...##"""
        output = """Possible"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
###
..#
###
#..
###"""
        output = """Impossible"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
##...
.###.
.###.
...##"""
        output = """Impossible"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
