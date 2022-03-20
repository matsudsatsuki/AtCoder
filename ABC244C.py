from ast import Num
from doctest import FAIL_FAST
import re


def resolve():
    N = int(input())
    if N == 0:
        exit()
    num_lis = [int(i) for i in range(2,(2*N)+2)]
    print(1,flush=True)
    while num_lis:
        n = int(input())
        num_lis.remove(n)
        a = num_lis.pop(0)
        print(a,flush=True)



    
    

        
        
        
    









