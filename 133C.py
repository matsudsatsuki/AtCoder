from ast import Break

from matplotlib.pyplot import flag


def resolve():
    L,R = map(int,input().split())
    ans = 1e10
    flag = False
    for i in range(L,R+1):
        for j in range(i+1,R+1):
            if i*j < 2019:
                ans = i*j
                flag = True
                break
            else:
                ans = min(ans,(i*j)%2019)
                if ans == 0:
                    flag = True
                    break
        if flag:
            break
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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
