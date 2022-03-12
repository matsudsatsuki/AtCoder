def resolve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans_1 = 0
    for a,b in zip(A,B):
        if a == b:
            ans_1 += 1
    ans_2 = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] == B[j]:
                ans_2 += 1
    ans = [ans_1,ans_2]
    for i in range(2):
        print(ans[i])





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
        input = """4
1 3 5 2
2 3 1 4"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2 3
4 5 6"""
        output = """0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
4 8 1 7 9 5 6
3 5 1 7 8 2 6"""
        output = """3
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
