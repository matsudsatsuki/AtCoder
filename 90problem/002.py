from sympy import im


def resolve():
    from itertools import product
    N = int(input())
    flag = True
    if N%2:
        flag = False
    if flag:
        for b in product([0,1],repeat=N):
            a = 0
            for i in range(N):
                if b[i] == 0:
                    a += 1
                else:
                    a -= 1
                if a < 0:
                    break
            if a != 0:
                continue
            print(''.join(['(' if b[i] == 0 else ')'for i in range(N)]))
    else:
        print('')







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
        input = """2"""
        output = """()"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4"""
        output = """(())
()()"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10"""
        output = """((((()))))
(((()())))
(((())()))
(((()))())
(((())))()
((()(())))
((()()()))
((()())())
((()()))()
((())(()))
((())()())
((())())()
((()))(())
((()))()()
(()((())))
(()(()()))
(()(())())
(()(()))()
(()()(()))
(()()()())
(()()())()
(()())(())
(()())()()
(())((()))
(())(()())
(())(())()
(())()(())
(())()()()
()(((())))
()((()()))
()((())())
()((()))()
()(()(()))
()(()()())
()(()())()
()(())(())
()(())()()
()()((()))
()()(()())
()()(())()
()()()(())
()()()()()"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
