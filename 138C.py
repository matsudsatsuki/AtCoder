from audioop import avg


def resolve():
    N = int(input())
    V = [int(x)for x in input().split()]
    V_sorted = sorted(V,reverse=True)
    #a = V_sorted.pop()
    #print(a)
    while len(V_sorted)!=1:
        min_1 = V_sorted.pop()
        min_2 = V_sorted.pop()
        avg = (min_1+min_2)/2
        V_sorted.append(avg)
    print(*V_sorted)








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
        input = """2
3 4"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
500 300 200"""
        output = """375"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
138 138 138 138 138"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
