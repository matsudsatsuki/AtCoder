from ast import Break


def resolve():
    N = int(input())
    def read():
        S = set()
        for y in range(N):
            l = input()
            for x in range(N):
                if l[x] == '#':
                    S.add((x,y))
        return S
    S = read()
    T = read()
    for _ in range(4):
        mx,my = min(S)
        S = set((x-mx,y-my) for x,y in S)
        mx,my = min(T)
        T = set((x-mx,y-my) for x,y in T)

        if S == T:
            print('Yes')
            exit(0)
        T = set((y,-x) for x,y in T)
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
        input = """5
.....
..#..
.###.
.....
.....
.....
.....
....#
...##
....#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
#####
##..#
#..##
#####
.....
#####
#..##
##..#
#####
....."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
#...
..#.
..#.
....
#...
#...
..#.
...."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
#...
.##.
..#.
....
##..
#...
..#.
...."""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
