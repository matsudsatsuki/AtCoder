def resolve():
    S = input()
    sum_list = []
    for i in range(len(S)-2):
        a = S[i]
        for j in range(i+1,i+3):
            a += S[j]
        a = int(a)
        sum_list.append(abs(a-753))
    print(min(sum_list))

        

   
   








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
        input = """1234567876"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """35753"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1111111111"""
        output = """642"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
