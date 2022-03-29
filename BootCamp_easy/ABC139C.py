from itertools import count


def resolve():
    N = int(input())
    H = list(map(int,input().split()))
    count = 0
    ans = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            count += 1
            ans = max(ans,count)
        else:
            ans = max(count,ans)
            count = 0
        
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
        input = """5
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
