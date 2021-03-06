def resolve():
    from collections import defaultdict
    N = int(input())
    S = input()
    d = defaultdict(int)
    mod = 10**9+7
    for s in S:
        d[s] += 1
    #print(d)
    ans = 1
    for v in d.values():
        ans *= v+1
    print((ans-1)%mod)









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
abcd"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
baa"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abcab"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
