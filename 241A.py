def resolve():
    x = [int(x)for x in input().split()]
    ans = [0]
    a = 0
    for i in range(3):
        a = x[a]
        ans.append(a)
    print(ans[-1])
    

    




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
        input = """9 0 1 2 3 4 5 6 7 8"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 8 8 8 0 8 8 8 8 8"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 0 0 0 0 0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
