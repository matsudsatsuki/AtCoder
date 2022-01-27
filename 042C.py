
N,K = map(int,input().split())

hate_num = [str(i) for i in input().split()]
pay = N


while True:
    flag = False
    for p in str(pay):
        if p in hate_num:
            pay += 1
            break
        else:
            print(pay)
            flag = True
            break
            
    if flag:
        break
