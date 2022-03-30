def resolve():
    N = int(input())
    B = list(map(int,input().split()))
    ans = []
    while B:
        for i in range(len(B)-1,-1,-1):
            if B[i] == i+1:
                B.remove(i+1)
                ans.append(i+1)
                break
        else:
            print(-1)
            break
    else:
        for i in reversed(ans):
            print(i)







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
1 2 1"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
2 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
1 1 1 2 2 1 2 3 2"""
        output = """1
2
2
3
1
2
2
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
