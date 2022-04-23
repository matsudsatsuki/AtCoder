from itertools import count


def resolve():
    A,B,C,D,E,F,X = map(int,input().split())
    if X >= A+C:
        t = ((X // (A+C))*A)*B
        t += (X % (A+C))*B
    if X >= D+F:
        e = (X // (D+F)*D)*E
        e += (X % (D+F))*E
    if X < A+C:
        if X < A:
            t = (A-X)*B
        else:
            t = A*B
    if X < D+F:
        if X < D:
            e = (D-X)*E
        else:
            e = D*E
    if t > e:
        print('Takahashi')
    if t < e:
        print('Aoki')
    if t == e:
        print('Draw')
    

    


    
        
    







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
        input = """4 3 3 6 2 5 10"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 4 1 5 9 2"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1 1 1 1 1"""
        output = """Draw"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

