def resolve():
    Q = int(input())
    A = []
    for i in range(Q):
        query = [int(x)for x in input().split()]
        if query[0] == 1:
            A.append(query[1])
        if query[0] == 2:
            A.sort()
            for j in range(len(A)):
                if A[j] >= query[1]:
                    if j - query[2] >= 0:
                        print(A[j-query[2]])
                    else:
                        print(-1)
        if query[0] == 3:
            print(query[2])
            A.sort(reverse=True)
            for l in range(len(A)):
                if A[l] <= query[1]:
                    if l + query[2] < len(A-1):
                        print(A[l+query[2]]) 
                    else:
                        print(-1)
                













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
        input = """11
1 20
1 10
1 30
1 20
3 15 1
3 15 2
3 15 3
3 15 4
2 100 5
1 1
2 100 5"""
        output = """20
20
30
-1
-1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
