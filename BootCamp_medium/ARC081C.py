


from audioop import reverse

from numpy import ediff1d


def resolve():
    import collections
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    d = dict(collections.Counter(A))
    #print(d.items())
    edge = []
    for a,b in reversed(d.items()):
        if b >= 4:
            edge.append(a)
            edge.append(a)
            break   
        if b >= 2 and len(edge) < 2:
            edge.append(a)
            if len(edge) == 2:
                break
    if len(edge) < 2:
        print(0)
    else:
        print(edge[0]*edge[1])

        


    










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
        input = """6
3 1 2 4 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
3 3 3 3 4 4 4 5 5 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
