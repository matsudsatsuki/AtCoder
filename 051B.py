def resolve():
    K,S = map(int,input().split())
    count = 0
    for x in range(K+1):
        for y in range(K+1):
            z = S - (x + y)
            if z >= 0 and z <= K:
                count += 1            
                

        
    print(count)






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
        input = """2 2"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 15"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
