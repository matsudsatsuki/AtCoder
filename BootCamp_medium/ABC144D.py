def resolve():
    import math
    a,b,x = map(int,input().split())
    volume = (a**2)*b
    if x > volume/2:
        ans = math.degrees(math.atan((2*b-2*x/a**2)/a))
    else:
        ans = math.degrees(math.atan(a*b**2/x/2))
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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
