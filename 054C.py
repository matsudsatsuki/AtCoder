from re import S

from aem import con


def resolve():
    
    N,M = map(int,input().split())
    G = [[]for _ in range(N)]
    for i in range(M):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    def DFS(start_list,s,cnt):
        start_list[s] = 1
        if sum(start_list) == N:
            cnt[0] += 1
        else:
            for node in G[s]:
                if start_list[node] == 0:
                    DFS(start_list[:node]+[1]+start_list[node+1:],node,cnt)
        return cnt[0]

    start_list = [0 for i in range(N)]
    cnt = [0]
    print(DFS(start_list,0,cnt))

    




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
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
