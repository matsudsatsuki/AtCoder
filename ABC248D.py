def resolve():
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    ANS=[0]*Q
    C=[0]*(N+1)
    que=[[] for i in range(N)]
    for i in range(Q):
            l,r,x=map(int,input().split())
            l-=1
            if l:

                que[l-1].append((i,x,-1))
            que[r-1].append((i,x,1))
    for i in range(N):
        C[A[i]]+=1
        for j in range(len(que[i])):
                ANS[que[i][j][0]]+=C[que[i][j][1]]*que[i][j][2]
    print(*ANS,sep='\n')
        






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
3 1 4 1 5
4
1 5 1
2 4 3
1 5 2
1 3 3"""
        output = """2
0
0
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
