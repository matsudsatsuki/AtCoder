def resolve():
    s = int(input())
    a = set()
    i = 0
    ans = 0
    while True:
        i += 1
        if s in a:
            ans = i
            break
        a.add(s)
        if s % 2 == 0:
            s //= 2
            continue
        elif s % 2 != 0:
            s = (3*s)+1 
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
        input = """8"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """54"""
        output = """114"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
