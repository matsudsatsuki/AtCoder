def resolve():
    from collections import defaultdict
    N = int(input())
    A = list(map(int,input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 0
    for k,v in d.items():
        if k-v < 0:
            ans += abs(k-v)
        elif k-v > 0:
            ans += v
        elif k-v == 0:
            continue
    if N < ans:
        ans = N
    print(ans)








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
3 3 3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 4 1 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 2 2 3 3 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """8
2 7 1 8 2 8 1 8"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
