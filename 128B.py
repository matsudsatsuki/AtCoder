def resolve():
    N = int(input())
    d = {}
    for i in range(1,N+1):
        key,value = input().split()
        d[i] = [key,int(value)]
        
    a = sorted(d.values(),key=lambda x:x[1],reverse=True)
    
    b = sorted(a,key=lambda x: x[0])
    #print(a)
    for b_item in b:
        for i in range(1,len(d)+1):
            if b_item == d[i]:
                print(i)
            else:
                continue
            
    


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
        input = """6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40"""
        output = """3
4
6
1
5
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
yakutsk 10
yakutsk 20
yakutsk 30
yakutsk 40
yakutsk 50
yakutsk 60
yakutsk 70
yakutsk 80
yakutsk 90
yakutsk 100"""
        output = """10
9
8
7
6
5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
