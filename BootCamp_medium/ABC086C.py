

def resolve():
    N = int(input())
    flag = True
    init_y,init_x = 0,0
    times = []
    x_list = []
    y_list = []
    for i in range(N):
        t,x,y = map(int,input().split())
        times.append(t)
        x_list.append(x)
        y_list.append(y)
    past_time = 0
    for i in range(N):
        if abs(init_x-x_list[i])+abs(init_y-y_list[i]) > abs(times[i]-past_time):
            flag = False
            break
        if abs(times[i]-past_time)%(abs(init_x-x_list[i])+abs(init_y-y_list[i])) == 0:
            init_x = x_list[i]
            init_y = y_list[i]
            past_time = times[i]
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
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()









