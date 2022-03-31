from matplotlib.pyplot import flag


def resolve():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    ca = Counter(a)

    def solve():
        if len(ca) > 3:
            return False
        kv = list(ca.items())
        if len(ca) == 1:
            return ca[0] == n
        if n % 3 != 0:
            return False
        if len(ca) == 2:
            return ca[0] == n//3
        xv, yv, zv = kv
        if xv[1] != n//3 or yv[1] != n//3 or zv[1] != n//3:
            return False
        return xv[0]^yv[0] == zv[0]

    print('Yes' if solve() else 'No')

  






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
        input = """3
1 2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
