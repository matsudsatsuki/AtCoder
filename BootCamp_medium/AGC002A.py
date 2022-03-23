def resolve():
    a,b = map(int,input().split())
    ans = 'Positive'
    if a <=0<=b:
        ans = 'Zero'
    elif a < 0 and b < 0:
        x = b-a+1
        if x % 2 != 0:
            ans = 'Negative' 
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


if __name__ == "__main__":
    unittest.main()
