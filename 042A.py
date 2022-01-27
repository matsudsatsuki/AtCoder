#5 5 7
a,b,c = map(int,input().split())

num_list = [a,b,c]
if num_list.count(5) == 2 and num_list.count(7) == 1:
    print('YES')
else:
    print('NO')