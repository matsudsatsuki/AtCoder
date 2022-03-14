def resolve():
    S = input()
    n = len(S)
    ans = 0
    for i in range(n):
        if S[i] == 'U':
            ans += n-1-i
            ans += 2*i
        else:
            ans += i
            ans += (2*(n-i-1))
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
        input = """UUD"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """UUDUUDUD"""
        output = """77"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
