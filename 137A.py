def resolve():
    A,B = map(int,input().split())
    ans_1 = A*B
    ans_2 = A+B
    ans_3 = A-B
    ans = max(ans_1,ans_2,ans_3)
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
        input = """-13 3"""
        output = """-10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 -33"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13 3"""
        output = """39"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
