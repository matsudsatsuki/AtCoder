from tkinter.tix import Tree

from aem import con


def resolve():
    N = int(input())
    scores = []
    for i in range(N):
        a = int(input())
        scores.append(a)
    max_score = sum(scores)
    scores.sort(reverse=True)
    flag = False
    score = 0
    if max_score % 10 != 0:
        score = max_score
    if max_score % 10 == 0:
        while scores:
            min_score = scores.pop()
            if min_score % 10 == 0:
                continue
            if min_score%10 != 0:
                score = max_score-min_score
                break
    if not scores:
        print(0)
    else:
        print(score)








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
        input = """3
5
10
15"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10
10
15"""
        output = """35"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
10
20
30"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
