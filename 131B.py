def resolve():
    N,L = map(int,input().split())
    apples = [int(i) for i in range(L,L+N)]
    abs_list = []
    for apple in apples:
        abs_list.append(abs(apple))
    a = min(abs_list)
    if a in apples:
        apples.remove(a)
        print(sum(apples))
    if -a in apples:
        apples.remove(-a)
        print(sum(apples)) 
    #ans = apples.remove(a)
    #print(sum(ans))
    







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
        input = """5 2"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 -1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 -50"""
        output = """-1044"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
