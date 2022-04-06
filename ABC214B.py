def resolve():
    S,T = map(int,input().split())
    ans = 0
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if S-(i+j+k)>= 0 and i*j*k <= T:
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
        input = """1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10"""
        output = """213"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """30 100"""
        output = """2471"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
