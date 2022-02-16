from itertools import count

from aem import con


def resolve():
    N = int(input())
    num_list = [int(x)for x in input().split()]
    #print(num_list)
    count = 0
    for i in range(1,N-1):
        if (num_list[i] != max(num_list[i-1],num_list[i],num_list[i+1])) and (num_list[i] != min(num_list[i-1],num_list[i],num_list[i+1])):
            count += 1
        else:
            continue
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
        input = """5
1 3 5 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
9 6 3 2 5 8 7 4 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
