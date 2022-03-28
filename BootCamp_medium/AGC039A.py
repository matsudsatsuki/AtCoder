from itertools import count


def resolve():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    a = []
    c = 1
    for i in range(1,n):
        if s[i-1] == s[i]:
            c += 1
        else:
            a.append(c)
            c = 1
    a.append(c)
    if len(a) == 1:
        print(a[0]*k//2)
    else:
        ans = 0
        if s[0] == s[-1]:
            ans += a[0] // 2 + a[-1] // 2
            a[0] += a[-1]
            ans += a[0]//2 * (k-1)
            for i in range(1,len(a)-1):
                    ans += a[i]//2*k
        else:
            for i in a:
                ans += i//2*k
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
        input = """issii
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """qq
81"""
        output = """81"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """cooooooooonteeeeeeeeeest
999993333"""
        output = """8999939997"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
