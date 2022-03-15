def resolve():
    N,M = map(int,input().split())
    ans = 0
    if N*2 <= M:
        ans += N
        M -= N*2
        ans += M//4
    else:
        ans += M//2
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
        input = """1 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12345 678901"""
        output = """175897"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
