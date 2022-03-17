def resolve():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    dis = []
    for i in range(1,N):
        dis.append(abs(A[i-1]-A[i]))
    dis.append(K-A[-1]+A[0])
    dis.sort()
    dis.pop()
    print(sum(dis))










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
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
