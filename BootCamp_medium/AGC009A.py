def resolve():
    N = int(input())
    A,B = [],[]
    ans = 0
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    for a,b in zip(reversed(A),reversed(B)):
        a += ans
        if a < b:
            if a == 0:
                continue
            else:
                ans += b-a
        if a > b:
            if a%b == 0:
                continue
            else:
                ans += b-(a%b)
        if a == b:
            continue
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
        input = """3
3 5
2 7
9 4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
3 1
4 1
5 9
2 6
5 3
5 8
9 7"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
