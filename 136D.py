def resolve():
    S = input()
    children = [0 for i in range(len(S))]
    print(children)
    r_counter = 0
    l_counter = 0
    #ans_list = [0 for num in range(2)]
    #ans_list  += [0 for num in range(2)]
    #print(ans_list)
    for i in range(len(S)-1):
        if S[i] == 'R':
            r_counter += 1
            if S[i+1] == 'L':
                if i+1 == len(S)-1:
                    children[i+1] = 1
                    children[i] = r_counter
                    break
                else:
                    children[i] = r_counter
                    r_counter = 0
        if S[i] == 'L':
            l_counter += 1
            if S[i+1] == 'R':
                children[(i-l_counter)+1] = l_counter
                l_counter = 0

    print(children)









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
        input = """RRLRL"""
        output = """0 1 2 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """RRLLLLRLRRLL"""
        output = """0 3 3 0 0 0 1 1 0 2 2 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """RRRLLRLLRRRLLLLL"""
        output = """0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
