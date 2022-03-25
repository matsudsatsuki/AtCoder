def resolve():
    from collections import deque
    A = input()
    B = input()
    C = input()
    A = deque(A)
    B = deque(B)
    C = deque(C)
    player = [0,1,2]
    p = 'a'
    while True:
        if p == 'a':
            if not A:
                winner = 'A'
                break
            p = A.popleft()
            continue
        elif p == 'b':
            if not B:
                winner = 'B'
                break
            p = B.popleft()
            
        elif p == 'c':
            if not C:
                winner = 'C'
                break
            p = C.popleft()
    print(winner)
        
    
            
    
        






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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
