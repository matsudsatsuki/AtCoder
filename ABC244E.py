def resolve():
    N,M,S,K,T,X = map(int,input().split())
    G = [[]for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    print(G)

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
        input = """4 4 4 1 3 2
1 2
2 3
3 4
1 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5 10 1 2 3
2 3
2 4
4 6
3 6
1 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 15 20 4 4 6
2 6
2 7
5 7
4 5
2 4
3 7
1 7
1 4
2 9
5 10
1 3
7 8
7 9
1 6
1 2"""
        output = """952504739"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

