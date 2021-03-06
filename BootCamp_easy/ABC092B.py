def resolve():
    N = int(input())
    D,X = map(int,input().split())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)
    ans = X
    for a in A:
        if D%a == 0:
            ans += D//a
        else:
            ans += (D//a)+1

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
        input = """3
7 1
2
5
10"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
8 20
1
10"""
        output = """29"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
30 44
26
18
81
18
6"""
        output = """56"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
