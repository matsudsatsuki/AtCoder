def resolve():
    A,B,K = map(int,input().split())
    ans = 0
    while A<B:
        A *= K
        ans += 1
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
        input = """1 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31 415926 5"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
