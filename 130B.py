def resolve():
    N,X = map(int,input().split())
    L = [int(x)for x in input().split()]
    #print(L)
    D = 0
    count = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            count += 1
        else:
            break
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
        input = """3 6
3 4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 9
3 3 3 3"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
