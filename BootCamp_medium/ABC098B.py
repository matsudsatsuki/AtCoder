from ast import Break


def resolve():
    import itertools
    N = int(input())
    S = input()
    s = []
    for i in range(len(S)):
        s.append(S[i])
    counter = []
    count = 0
    is_in = set()
    for i in range(N-1):
        a = s[:i+1]
        b = s[i+1:]
        for c in a:
            #print(c)
            if c in is_in:continue
            is_in.add(c)
            if c in b:
                count += 1
        counter.append(count)
        count = 0
        is_in.clear()
    print(max(counter))
            
            





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
        input = """6
aabbca"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
