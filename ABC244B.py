def resolve():
    N = int(input())
    T = input()
    states = ['E','S','W','N']
    state = 0
    x,y = 0,0
    for i in range(N):
        if T[i] == 'R':
            state += 1
        elif T[i] == 'S':
            if states[state%4] == 'E':
                x += 1
            if states[state%4] == 'S':
                y -= 1
            if states[state%4] == 'W':
                x -= 1
            if states[state%4] == 'N':
                y += 1
    print(x,y)





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
        input = """4
SSRS"""
        output = """2 -1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
SRSRSSRSSSRSRRRRRSRR"""
        output = """0 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
