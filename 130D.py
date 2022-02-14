from itertools import count

from aem import con


def resolve():
    N,K = map(int,input().split())
    n_list = [int(x)for x in input().split()]
    left = 0
    count = 0
    ans = 0
    for right in range(N):
        count += n_list[right]
        while count >= K:
            ans += N-right
            count -= n_list[left]
            left += 1 


            
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
        input = """4 10
6 1 2 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
3 3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352"""
        output = """36"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
