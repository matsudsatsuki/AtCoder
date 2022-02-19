def resolve():
    N,M = map(int,input().split())
    G = [[]for i in range(N)]

    for i in range(M):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    
    def walk(G,s,S=set()):
        P,Q = dict(),set()
        P[s] = None
        Q.add(s)
        while Q:
            u = Q.pop()
            for v in G[u].difference(P,S):
                Q.add(v)
                P[v] = u
        return P

    def components(G):
        comp = []
        seen = set()
        for u in G:
            if u in seen:
                continue
            C = walk(G,u)
            seen.update(C)
            comp.append(C)
        return comp
    
    #print(component)            











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

    def test_入力例1(self):
        input = """8 7
1 2
2 3
2 4
5 6
6 7
6 8
7 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 1
1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """11 11
1 2
1 3
2 4
3 5
4 6
5 7
6 8
7 9
8 10
9 11
10 11"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
