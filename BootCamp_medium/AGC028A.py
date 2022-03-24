from math import gcd


def resolve():
    from collections import defaultdict
    from math import gcd
    N,M = map(int,input().split())
    S = input()
    T = input()
    d = defaultdict(int)
    def lcm(a,b):
        return a*b//gcd(a,b)
    l = lcm(N,M)
    flag = True
    for i in range(N):
        d[l*i//N] = S[i]
    for j in range(M):
        if l*j//M in d and d[l*j//M] != T[j]:
            flag = False
    print(l if flag else -1)
    




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
        input = """3 2
acp
ae"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3
abcdef
abc"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 9
dnsusrayukuaiia
dujrunuma"""
        output = """45"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
