def resolve():
    S = input()
    ans = 0
    def reverse(n):
        if n == '0':
            return '1'
        elif n == '1':
            return '0'
    S = list(S)
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            if i+2 < len(S):
                if S[i] == S[i+2]:
                    ans += 1
                    S[i+1] = reverse(S[i+1])
                elif S[i] != S[i+2]:
                    ans += 2
                    S[i+1] = reverse(S[i+1])
                    S[i+2] = reverse(S[i+2])
            else:
                ans += 1
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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
