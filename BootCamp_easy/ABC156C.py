def resolve():
    N = int(input())
    p = [int(x)for x in input().split()]
    min_n = min(p)
    max_n = max(p)
    ans = 1e9
    for i  in range(min_n,max_n+1):
        sum = 0
        for j in range(len(p)):
            sum += (p[j]-i)**2
        ans = min(ans,sum)
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
        input = """2
1 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
14 14 2 13 56 2 37"""
        output = """2354"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
