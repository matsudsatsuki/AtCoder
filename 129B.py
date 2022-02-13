


def resolve():
    N = int(input())
    num_list = [int(x)for x in input().split()]
    #print(num_list)
    ans_list = []
    for i in range(N):
        part_list = num_list[i+1:]
        part_sum = sum(part_list)
        ans = abs(part_sum - sum(num_list[:i+1]))
        ans_list.append(ans)
    print(min(ans_list))

        



        














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
1 2 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 3 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
27 23 76 2 3 5 62 52"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
