from itertools import count


def resolve():
    H,W = map(int,input().split())
    S = [list(input())for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if S[y][x] == '.':
                S[y][x] = 0
    count = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == '#':
                continue
            if y > 0 and S[y - 1][x] == '#':
                count += 1
            if y < H - 1 and S[y + 1][x] == '#':
                count += 1
            if x > 0 and S[y][x - 1] == '#':
                count += 1
            if x < W - 1 and S[y][x + 1] == '#':
                count += 1
            if y > 0 and x > 0 and S[y-1][x-1] == '#':
                count += 1
            if y > 0 and x < W - 1 and S[y-1][x+1] == '#':
                count += 1
            if y < H-1 and x > 0 and S[y+1][x-1] == '#':
                count += 1
            if y < H-1 and x < W-1 and S[y+1][x+1] == '#':
                count += 1
            S[y][x] = count
            count = 0

    for i in S:
        print(''.join(map(str,i)))
                











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
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
