

def resolve():
    from collections import defaultdict
    N = int(input())
    dict = defaultdict(int)
    for _ in range(N):
        a = input()
        dict[a[0]] += 1
    ans = 0
    t = 'MARCH'
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                ans += dict[t[i]] * dict[t[j]] * dict[t[k]]
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
        input = """5
MASHIKE
RUMOI
OBIRA
HABORO
HOROKANAI"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
ZZ
ZZZ
Z
ZZZZZZZZZZ"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
CHOKUDAI
RNG
MAKOTO
AOKI
RINGO"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
