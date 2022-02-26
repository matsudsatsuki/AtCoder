from tkinter.tix import Tree

from pyrsistent import T


def resolve():
    class Node:
        def __init__(self):
            self.parent = -1
            self.children = []
        
    def cal_depth(node_id,d=0):
        Tree[node_id].depth = d
        for child in Tree[node_id].children:
            cal_depth(child,d+1)
    N,Q = map(int,input().split())
    Tree = [Node()for _ in range(N)]
    print(Tree)

    #make tree
    for _ in range(N):
        #id,child_n,
        tree_info = list(map(int,input().split()))
        node_id = tree_info[0]
        k = tree_info[1]
        if k > 0:
            children = tree_info[2:]
            Tree[node_id].children = children
            Tree[node_id].type = 'internal node'
        else:
            Tree[node_id].type = 'leaf'
        for child in Tree[node_id].children:
            Tree[child].parent = node_id





    



    












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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
