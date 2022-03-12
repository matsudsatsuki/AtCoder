


def resolve():
    N = int(input())
    X,Y = [],[]
    for _ in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    S = input()
    flag = True
    a = []
    INF = 1e5
    dp = [-1]*int(INF)
    for i in range(N):
        dp[Y[i]] = max(X[i],dp[Y[i]])
    dp_2 = [1e9]*int(INF)
    for i in range(N):
        dp_2[Y[i]] = min(X[i],dp[Y[i]])
    for i in range(N):
        if dp[Y[i]] == -1 or dp_2[Y[i]]== 1e9:continue
        if dp[Y[i]] > X[i] and S[i] == 'R':
            flag = False
            break
        if dp_2[Y[i]] < X[i] and S[i] == 'L':
            flag = False
            break

    


   
    if flag:
        print('No')
    else:
        print('Yes')




    



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
2 3
1 1
4 1
RRL"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 1
2 1
RR"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
