def resolve():
    num = input()
    #print(num)
    ans = 0
    for bit in range(1<<(len(num)-1)):
        t = int(num[0]) 
        for j in range(len(num)-1):
            if bit&(1<<j):
                t += int(num[j+1])
            else:
                t -= int(num[j+1])
        if t == 7:
            a = num[0]
            for j in range(len(num)-1):
                if bit&(1<<j):
                    a += '+'
                else:
                    a += '-'
                a += num[j+1]
    a += '=7'
    print(a)


        








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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
