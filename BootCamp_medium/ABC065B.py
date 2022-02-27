from itertools import count
from aem import con
from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    botan = []
    flag = False
    for i in range(N):
        a = int(input())
        botan.append(a)
    count = 0
    i = 0
    j = 0
    while j < N:
        count += 1
        b = botan[i]-1
        i = b
        j += 1
        if b == 1:
            flag = True
            break
    if flag:
        print(count)
    else:
        print(-1)
        

        

        





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
        input = """3
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
