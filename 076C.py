from matplotlib.pyplot import flag


def resolve():
    S = input()
    T = input()
    n = len(S)
    m = len(T)
    p = -1
    ans = []
    for i in range(n-m+1):
        flag = True
        for j in range(i,i+m):
            if S[j] == '?' or S[j] == T[j-i]:
                continue
            else:
                flag = False
                break
        if flag:
            p = i
    flag2 = True
    for i in range(n):
        if p == -1:
            print('UNRESTORABLE')
            flag2 = False
            break
        if p <= i <= p+m-1:
            ans.append(T[i-p])
        elif S[i] == '?':
            ans.append('a')
        else:
            ans.append(S[i])

    if flag2:
        print(''.join(ans))


 
    
    

                
            
                
            








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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

    