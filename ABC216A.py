def resolve():
    X = input()
    #print(len(X))
    if len(X) == 4:
        if int(X[-1]) <= 2:
            print(X[:2]+'-')
        elif  3 <= int(X[-1]) <= 6:
            print(X[:2])
        else:
            print(X[:2]+'+')
    if len(X) == 3:
        if int(X[-1]) <= 2:
            print(X[0]+'-')
        elif  3 <= int(X[-1]) <= 6:
            print(X[0])
        else:
            print(X[0]+'+')


    
    








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
        input = """15.8"""
        output = """15+"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1.0"""
        output = """1-"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12.5"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
