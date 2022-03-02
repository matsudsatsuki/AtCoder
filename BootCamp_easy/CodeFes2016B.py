from appscript import con


def resolve():
    N,A,B = map(int,input().split())
    S = input()
    passed = 0
    fore_pass = 0
    for i in range(len(S)):
        if S[i] == 'a' and passed < A+B:
            print('Yes')
            passed += 1
            continue
        if S[i] == 'b' and passed < A+B and fore_pass < B:
            print('Yes')
            fore_pass += 1
            passed += 1
            continue
        else:
            print('No')








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
        input = """10 2 3
abccabaabb"""
        output = """Yes
Yes
No
No
Yes
Yes
Yes
No
No
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 5 2
cabbabaacaba"""
        output = """No
Yes
Yes
Yes
Yes
No
Yes
Yes
No
Yes
No
No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2 2
ccccc"""
        output = """No
No
No
No
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
