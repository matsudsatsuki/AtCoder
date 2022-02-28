from ast import Break
from aem import con


def resolve():
    S = input()
    s = []
    for i in range(len(S)):
        s.append(S[i])
    ans = 0
    while s:
        s.pop(-1)
        if len(s) % 2 == 0:
            if s[len(s)//2:] == s[:len(s)//2]:
                ans = len(s)
                break
        else:
            continue
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
        input = """abaababaab"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """xxxx"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcabcabcabc"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """akasakaakasakasakaakas"""
        output = """14"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
