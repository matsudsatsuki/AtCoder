def resolve():
    X = input()
    flag = False
    if X[0] == X[1] == X[2] == X[3]:
        flag = False
    else:
        for i in range(1,4):
            if int(X[i-1])+1 == int(X[i]) or (int(X[i-1]) == 9 and int(X[i]) == 0):
                continue
            else:
                flag = True
                break
                
    if flag:
        print('Strong')
    else:
        print('Weak')









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
        input = """7777"""
        output = """Weak"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """Strong"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9012"""
        output = """Weak"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
