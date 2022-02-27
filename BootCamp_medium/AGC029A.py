from matplotlib.pyplot import flag


def resolve():
    import re
    S = input()
    count = 0
    while True:
        m = re.findall(r'BW',S)
        S = re.sub(r'BW','WB',S)
        if len(m) == 0:
            break
        else:
            count += len(m)
    print(count)











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
        input = """BBW"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """BWBWBW"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
