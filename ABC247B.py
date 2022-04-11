from doctest import FAIL_FAST
from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    S,T = [],[]
    for _ in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        flag = False
        for s in [S[i],T[i]]:
            is_s = True
            for j in range(N):
                if i != j:
                    if s == S[j] or s == T[j]:
                        is_s = False
            if is_s:
                flag = True
    print('No' if not flag else 'Yes')












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
tanaka taro
tanaka jiro
suzuki hanako"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
aaa bbb
xxx aaa
bbb yyy"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
tanaka taro
tanaka taro"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
takahashi chokudai
aoki kensho
snu ke"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
