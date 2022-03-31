def resolve():
    import string
    S=input()
    if len(S) < 26:
        print(S + min(c for c in string.ascii_lowercase if c not in S))
    else:
        for i in range(24, -1, -1):
            if S[i] < S[i + 1]:
                print(S[:i] + min(c for c in S[i:] if c > S[i]))
                break
        else:
            print(-1)


        

            

        





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
        input = """atcoder"""
        output = """atcoderb"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abc"""
        output = """abcd"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """zyxwvutsrqponmlkjihgfedcba"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """abcdefghijklmnopqrstuvwzyx"""
        output = """abcdefghijklmnopqrstuvx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
