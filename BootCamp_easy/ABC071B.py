from itertools import zip_longest
from re import X


def resolve():
    from itertools import zip_longest
    S = input()
    s_list = []
    for s in S:
        s_list.append(ord(s))
    s_list.sort()
    s_list = list(set(s_list))
    alpha = [x for x in range(ord('a'),ord('z')+1)]
    ans = 'None'
    for s,a in zip_longest(s_list,alpha):
        if s != a:
            ans = chr(a)
            break
    print(ans if alpha != s_list else 'None')







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
        input = """atcoderregularcontest"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcdefghijklmnopqrstuvwxyz"""
        output = """None"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg"""
        output = """d"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
