def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    min_a = min(A)
    max_a = max(A)
    costs = []
    if len(set(A)) == 1:
        print(0)
        exit()
    else:
        for i in range(min_a,max_a+1):
            cost = 0
            for a in A:
                cost += (a-i)**2
            costs.append(cost)   
    print(min(costs))






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
        input = """2
4 8"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
4 2 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
-100 -100 -100 -100"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
