from this import d


def resolve():
    N,M = map(int,input().split())
    #default_list = {int(i):False for i in range(1,N+1)}
    #print(default_list)
    ans_list = set()
    for i in range(M):
        a,b = map(int,input().split())
        if i == 0:
            tmp = [int(i) for i in range(a,b+1)]
            ans_list = set(tmp)
            continue
        else:
            tmp = [int(i) for i in range(a,b+1)]
            ans_list = ans_list & set(tmp)
    
    print(len(ans_list))
            
        
        




        
        

        









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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
