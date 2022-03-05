from itertools import count


def resolve():
    N,K = map(int,input().split())
    ans = 0
    i = 0
    while i < N:
        i += 1
        num = i
        count = 0
        while num < K:
            count += 1
            num *= 2
        coin = (1/2)**count
        #print(count)
        ans += (1/N) * coin
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
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
