from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    s = set()
    flag = True
    for _ in range(N):
        a = input()
        if a in s:
            flag = False
            break
        s.add(a)
    print('No' if flag else 'Yes')









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
sato hanako
tanaka taro"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
saito ichiro
saito jiro
saito saburo"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
sypdgidop bkseq
bajsqz hh
ozjekw mcybmtt
qfeysvw dbo"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
