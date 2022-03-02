from itertools import count
from tkinter.tix import Tree




def resolve():
    H,W = map(int,input().split())
    S = [list(input())for i in range(H)]
    flag = True

    for y in range(H):
        for x in range(W):
            if S[y][x] == '#':
                count = 0
                if y < H-1 and S[y+1][x] == '#':
                    count += 1 
                if y > 0 and S[y-1][x] == '#':
                    count += 1
                if x < W-1 and S[y][x+1] == '#':
                    count += 1
                if x > 0 and S[y][x-1] == '#':
                    count += 1
                if count == 0:
                    flag = False
                    break
    if flag:
        print('Yes')
    else:
        print('No')




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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
