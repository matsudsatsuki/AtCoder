def resolve():
    V,A,B,C  = map(int,input().split())
    a = [A,B,C]
    ans = 1
    i = 0
    while True:
        if V < a[i%3]:
            ans = i%3
            break
        V -= a[i%3]
        i += 1
    if ans == 0:
        print('F')
    if ans == 1:
        print('M')
    if ans == 2:
        print('T')

    





import sys
from io import BufferedRWPair, StringIO
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
        input = """25 10 11 12"""
        output = """T"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 10 10 10"""
        output = """F"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1 1 1"""
        output = """M"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
