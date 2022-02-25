from itertools import count


def resolve():
    import collections
    N = int(input())
    anagrams = []
    for i in range(N):
        a = input()
        anagrams.append(a)
    new = []
    for str in anagrams:
        a = collections.Counter(str)
        b = sorted(a.most_common())
        new.append(b)
    #print(b)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if new[i] == new[j]:
                ans += 1
    print(ans)
    count = 0
    for i in range(N):
        c = collections.Counter(anagrams[i])
        d = sorted(c.most_common())
        for j in range(i+1,N):
            e = collections.Counter(anagrams[j])
            f = sorted(e.most_common())
            #print(c,e)
            if d == f:
                count += 1

        #print(c.most_common())
    #print(count)
    #for str in anagrams:
        #a = collections.Counter(str)
        #b = a.most_common()
        #print(sorted(b))








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
acornistnt
peanutbomb
constraint"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
oneplustwo
ninemodsix"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
