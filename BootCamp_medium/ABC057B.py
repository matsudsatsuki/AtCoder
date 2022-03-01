from cmath import inf


def resolve():
    N,M = map(int,input().split())
    st = []
    for _ in range(N):
        a,b = map(int,input().split())
        st.append([a,b])
    #print(st)
    check_points = []
    for _ in range(M):
        a,b = map(int,input().split())
        check_points.append([a,b])
    inf = 1e9
    dis_lis = [[inf,None]for i in range(N)]

    for i in range(N):
        for j in range(M):
            dis = abs(st[i][0]-check_points[j][0])+abs(st[i][1]-check_points[j][1])
            a = dis_lis[i][0]
            if dis == dis_lis[i]:
                continue
            if dis < a:
                dis_lis[i] = [dis,j+1]

    for i in range(N):
        print(dis_lis[i][1])
            


            








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
        input = """2 2
2 0
0 0
-1 0
1 0"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5"""
        output = """3
1
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000"""
        output = """5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
