def resolve():
    N = int(input())
    L = [2,1]
    for i in range(2,N+1):
        L.append(L[i-2]+L[i-1])
    print(L[-1])












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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
