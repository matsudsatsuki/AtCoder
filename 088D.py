def resolve():
    import heapq
    H,W = map(int,input().split())
    G = [list(input())for _ in range(H)]
    INF = 1e9
    count = 0
    for y in range(H):
        for x in range(W):
            if G[y][x] == '#':
                G[y][x] = INF
                count += 1

            else:
                G[y][x] = 1     
    #print(G)
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    class State:
        def __init__(self,x,y,cost,ref): 
            self.x = x
            self.y = y
            self.cost = cost
            self.ref = ref
        def __hash__(self):
            return(self.x<<16) | self.y 
        def __eq__(self,others):
            return self.x == others.x and self.y == others.y
        def __lt__(self,others):
            return self.cost < others.cost

    def dijkstra(h,w,t,sx,sy,gx,gy):
        open_list  = []
        heapq.heapify(open_list)
        closed = set()
        init_state = State(sx,sy,t[sy][sx],None)
        heapq.heappush(open_list,init_state)
            
        while open_list:
            st = heapq.heappop(open_list)
            
            if st.x == gx and st.y == gy:
                return st
            if st in closed:
                continue
            closed.add(st)
            
            for i in range(4):
                nx = st.x + dx[i]
                ny = st.y + dy[i]
                if not (0 <= nx <=  w-1 and 0 <= ny <= h-1):
                    continue
                ncost = st.cost + t[ny][nx]
                heapq.heappush(open_list,State(nx,ny,ncost,st))
        return None

    st = dijkstra(H,W,G,0,0,W-1,H-1)
    shortest = st.cost
    if shortest == None:
        print(-1)
    else:
        ans = (W*H)-shortest-count
        print(ans)
    
    
    
    
    #while st is None:
        #print(st.y, st.x)
        #st = st.ref 

    







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
        input = """3 3
..#
#..
..."""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 37
.....................................
...#...####...####..###...###...###..
..#.#..#...#.##....#...#.#...#.#...#.
..#.#..#...#.#.....#...#.#...#.#...#.
.#...#.#..##.#.....#...#.#.###.#.###.
.#####.####..#.....#...#..##....##...
.#...#.#...#.#.....#...#.#...#.#...#.
.#...#.#...#.##....#...#.#...#.#...#.
.#...#.####...####..###...###...###..
....................................."""
        output = """209"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
