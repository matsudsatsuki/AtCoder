def resolve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    flag = [0]*N
    ans = 0
    for i in range(N):
        if i-K>=0 and T[i-K] == T[i] and flag[i-K]:
            continue
        if T[i] == 'r':
            ans+=P
        elif T[i] == 's':
            ans+=R
        else:
            ans+=S
        flag[i] = True
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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
