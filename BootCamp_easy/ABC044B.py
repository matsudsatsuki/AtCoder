from collections import defaultdict

from matplotlib.pyplot import flag


def resolve():
    from collections import defaultdict
    d = defaultdict(int)
    W = input()
    for w in W:
        d[w] += 1
    flag = True
    for v in d.values():
        if v % 2 != 0:
            flag = False
    print('Yes' if flag else 'No')
    








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
        input = """abaccaba"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hthth"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
