from sklearn.datasets import fetch_kddcup99


def resolve():
    N,M = map(int,input().split())
    A = [int(x)for x in input().split()]
    B = [int(x)for x in input().split()]
    flag = True
    for i in range(M):
        if B[i] in A:
            A.remove(B[i])
            continue
        else:
            flag = False
            break

    if flag:
        print('Yes')
    else:
        print('No')








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
        input = """3 2
1 1 3
3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
1000000000
1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
1 2 3 4 5
5 5"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
