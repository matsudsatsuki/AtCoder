def resolve():
    L,R = map(int,input().split())
    ans = 2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            if ans == 0:
                print(ans)
                exit()
            else:
                ans = min(ans,(i*j)%2019)
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
        input = """2020 2040"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
