from itertools import count
from aem import con


def resolve():
    N = int(input())
    A = [int(x)for x in input().split()]
    B = [int(x)for x in input().split()]
    count = 0
    res = 0
    for i in range(len(B)):
        if A[i] >= B[i]:
            count += B[i]
            continue
        if A[i] < B[i]:
            count += A[i]
            res = B[i]-A[i]
            if A[i+1] < res:
                count += A[i+1]
                A[i+1] = 0
                continue
            else:
                count += res
                A[i+1] -= res
                continue
    print(count)

        
        



           











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
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
