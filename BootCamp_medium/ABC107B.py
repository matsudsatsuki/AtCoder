from itertools import count
from aem import con


def resolve():
    H,W = map(int,input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        c = True
        for j in range(W):
            if a[i][j]=="#":
                c = False
                break
        if not c:
            b.append(a[i])
        else:
            H -= 1
    A = []
    for i in range(W):
        d = True
        for j in range(H):
            if b[j][i]=="#":
                d = False
                break
        if d:
            A.append(i)

    for i in range(H):
        B = []
        for j in range(W):
            if j not in A:
                B.append(b[i][j])
        print("".join(B))
    

    



    

        

    









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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
