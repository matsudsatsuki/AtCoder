


def resolve():
    D,G = map(int,input().split())
    num_list = []
    p = []
    c = []
    for i in range(D):
        a,b = map(int,input().split())
        p.append(a)
        c.append(b)
    ans = 1e9
    for bit in range(1<<(D)):
        pnt = 0
        num = 0
        for i in range(D):
            if (bit&(1<<i)):
                pnt += 100*(i+1)*p[i]+c[i]
                num += p[i]
        if pnt >= G:
            ans = min(ans,num)
        else:
            for j in range(D)[::-1]:
                if (bit&(1<<j)):
                    continue
                target = G-pnt
                if target <= (p[j]-1)*(100*(j+1)):
                    num += -(-target//(100*(j+1)))
                    ans = min(ans,num)
                else:
                    pnt += 100*(j+1)*(p[j]-1)
                    num += p[j]
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
        input = """2 700
3 500
5 800"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2000
3 500
5 800"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 400
3 500
5 800"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 25000
20 1000
40 1000
50 1000
30 1000
1 1000"""
        output = """66"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
