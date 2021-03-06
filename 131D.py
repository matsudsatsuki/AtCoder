from os import times
from matplotlib.pyplot import flag
from sqlalchemy import false
from sympy import principal_branch


def resolve():
    N = int(input())
    time_list = []
    close_time = []
    deadline = []
    for _ in range(N):
        a,b = map(int,input().split())
        time_list.append(a)
        close_time.append(b)
        c = b-a
        deadline.append(c)
    deadlines = []
    for k,v in zip(deadline,time_list):
        deadlines.append((k,v))
    time = max(close_time)
    deadlines.sort(key=lambda x: x[0])
    count = 0
    flag = True
    for e_deadline,times in deadlines:
        if count > e_deadline:
            flag = False
        count += times 
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
2 4
1 9
1 8
4 9
3 12"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
334 1000
334 1000
334 1000"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
384 8895
1725 9791
170 1024
4 11105
2 6
578 1815
702 3352
143 5141
1420 6980
24 1602
849 999
76 7586
85 5570
444 4991
719 11090
470 10708
1137 4547
455 9003
110 9901
15 8578
368 3692
104 1286
3 4
366 12143
7 6649
610 2374
152 7324
4 7042
292 11386
334 5720"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
