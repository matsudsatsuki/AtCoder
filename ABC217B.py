def resolve():
    S1 = input()
    S2 = input()
    S3 = input()
    c = ['ABC','ARC','AGC','AHC']
    lis = [S1,S2,S3]
    for a in lis:
        if a in c:
            c.remove(a)
        
    print(''.join(c))







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
        input = """ARC
AGC
AHC"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AGC
ABC
ARC"""
        output = """AHC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
