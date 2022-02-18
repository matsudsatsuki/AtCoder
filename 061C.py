from multiprocessing.connection import answer_challenge


def resolve():
    S = input()
    ans = 0
    for i in range(2**(len(S)-1)):
        tmp = S[0]

        for j in range(1,len(S)):
            if i % 2:
                ans += int(tmp)
                tmp = ''
            tmp += S[j]
            i >>= 1

        ans += int(tmp)
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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
