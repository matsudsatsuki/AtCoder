def resolve():
    N = int(input())
    board =[list(input())for i in range(N)]
    def row():
        result = "D"
        for line in board:
            pivot = line[0]
            count = 0

            for stone in line:
                if stone != "." and stone == pivot:
                    count += 1
                else:
                    break

            if count == 4:
                result = pivot
                break

        return result
    def column():
        result = "D"

        for i in range(5):
            pivot = ""
            count = 0

            for j in range(5):
                if pivot == "":
                    pivot = board[j][i]

                stone = board[j][i]
                if stone != "." and stone == pivot:
                    count += 1
                else:
                    break

            if count == 4:
                result = pivot
                break

        return result
    
    def oblique():
        result = "D"
        direction = [True, False]

        for reverse in direction:
            pivot = ""
            count = 0

            if reverse:
                j = 0
                j_diff = 1
            else:
                j = 4
                j_diff = -1

            for i in range(5):

                stone = board[i][j]

                if pivot == "":
                    pivot = stone

                if stone != "." and stone == pivot:
                    count += 1

                j = j + j_diff

            if count == 4:
                result = pivot
                break

        return result
    row = row()
    column = column()
    oblique = oblique()
    if row != 'D' and column != 'D' and oblique != 'D':
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


