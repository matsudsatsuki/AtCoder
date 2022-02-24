from heapq import heapify
from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    n_list = [int(x)for x in input().split()]
    max_list = [n_list[0]]
    flag = True
    for i in range(1,len(n_list)):
        top = max_list[-1]
        if n_list[i] > top:
            max_list.append(n_list[i])
        if n_list[i] < top:
            if n_list[i] == top-1:
                continue
            else:
                flag = False
                break
    if flag:
        print('Yes')
    else:
        print('No')

    
    
    

    
        








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
1 2 1 1 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 3 2 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 2 3 4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1000000000"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
