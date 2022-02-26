from itertools import count

from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    S = [list(input())for i in range(N)]
    #print(S)
    flag_1 = False
    row = 0
    flag = True
    for i in range(len(S)):#row_check
        count = 0
        out = 0
        flag = True
        for j in range(N):
            if S[i][j] == '#':
                count += 1
                if count == 4 and flag:
                    flag_1 = True
            if S[i][j] == '.':
                out += 1
                if out == 2:
                    flag == False
    #column
    flag_3 = False
    for i in range(N):
        count_2 = 0
        out_2 = 0
        flag_2 = True
        for j in range(N):
            if S[j][i] == '#':
                count_2 += 1
                if count_2 == 4 and flag_2:
                    flag_3 = True
            if S[j][i] == '.':
                out += 1
                if out == 2:
                    flag_2 = False
    #cross
    count_3 = 0
    out_3 = 0
    flag_4 = True
    flag_5 = False
    for i in range(N):
        if S[i][i] == '#':
            count_3 += 1
            if count_3 == 4 and flag_4:
                flag_5 = True
        if S[i][i] == '.':
            out_3 += 1
            if out_3 == 2:
                flag_4 = False
    count_4 = 0
    out_4 = 0
    flag_6 = True
    flag_7 = False
    for i in range(N-1,0,-1):
        if S[i][i] == '#':
            count_4 += 1
            if count_4 == 4 and flag_6:
                flag_7 = True
        if S[i][i] == '.':
            out_4 += 1
            if out_4 == 2:
                flag_6 = False
    if flag_1 or flag_3 or flag_5 or flag_7:
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
        input = """8
........
........
.#.##.#.
........
........
........
........
........"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
######
######
######
######
######
######"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
..........
#..##.....
..........
..........
....#.....
....#.....
.#...#..#.
..........
..........
.........."""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
