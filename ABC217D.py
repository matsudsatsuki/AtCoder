

from ast import If
from pandas import cut


def resolve():
    import bisect   
    import heapq
    L,Q = map(int,input().split())
    cuts = []
    heapq.heapify(cuts)
    heapq.heappush(cuts,L)
    for _ in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            heapq.heappush(cuts,x)
        if c == 2:
            if len(cuts) == 1:
                print(cuts[0])
            else:
                a = bisect.bisect_left(cuts,x)
                if a != 0:
                    print(cuts[a-1])
                else:
                    print(cuts[a])
    











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
        input = """5 3
2 2
1 3
2 2"""
        output = """5
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
1 2
1 4
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 10
1 31
2 41
1 59
2 26
1 53
2 58
1 97
2 93
1 23
2 84"""
        output = """69
31
6
38
38"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
