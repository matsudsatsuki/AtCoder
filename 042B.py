


N,L = map(int,input().split())
word_list = []

for i in range(N):
    word_list.append(input())

print(''.join(sorted(word_list)))

