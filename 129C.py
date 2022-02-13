from curses import beep


def resolve():
    N,M = map(int,input().split())
    break_list = []
    for i in range(M):
        a = int(input())
        break_list.append(a)
    #print(break_list)
    stairs = []
    for i in range(N+1):
        if i in break_list:
            stairs.append(False)
            continue
        else:
            stairs.append(i)
    j = 1
    ans = 0
    ans_list = []
    flag = False
    for i in range(1,N+1):
        if stairs[i] == False:
            if stairs[i+1] == False:
                ans = 0
                break
            else:
                flag = True
                j = 1
                ans_list.append(ans)
                ans = 0
                continue
        else:
            ans += j
            j += 1


    
    tmp_ans = 1
    if flag and ans != 0:
        for i in range(len(ans_list)):
            tmp_ans *= ans_list[i]
        fin_ans = tmp_ans%1000000007
        print(fin_ans)
    
        
    elif ans != 0:
        fin_ans = ans%1000000007
        print(fin_ans)
    else:
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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
