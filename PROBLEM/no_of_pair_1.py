from functools import total_ordering
'''
1
4
1111
6
'''

t=int(input("case"))
while(t!=0):
    n=int(input("size"))
    li=list(input("number"))
    c=li.count("1")
    total=c*(c-1)
    print(int(total/2))
    t=-1