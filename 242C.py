from aem import con
from matplotlib.pyplot import flag


def resolve():
    N = int(input())
    n = 998244353
    ans = 0
    
    for i in range(10**(N-1),10**N):
        stri = str(i)
        count = 1
        if '0' in stri:
            continue
        
        for j in range(1,N):
            a = stri[j-1]
            b = stri[j]
            a = int(a)
            b = int(b)
            if abs(a-b) <= 1:
                count += 1
            else:
                continue
        if count == N:
            ans += 1
        else:
            continue
                
    #print(stri)
    print(ans%n)

    





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
        input = """4"""
        output = """203"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """25"""
        self.assertIO(input, output)

    #def test_入力例_3(self):
        #input = """1000000"""
        #output = """248860093"""
        #self.assertIO(input, output)
    def test_入力例_4(self):
        input = """3"""
        output = """69"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()
