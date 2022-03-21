from collections import defaultdict
from email.policy import default
from cachetools import Cache


def resolve():
    from collections import defaultdict
    N = int(input())
    S = defaultdict(int)
    for _ in range(N):
        s = input()
        s = list(s)
        s.sort()
        s = ''.join(s)
        S[s] += 1
    ans = 0
    for v in S.values():
        ans += v*(v-1)//2
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
        input = """3
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
