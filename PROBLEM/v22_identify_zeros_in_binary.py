from typing import Counter
'''
 number:68
which form:2
3
'''

def fun1(n,b):
    output=""
    while n >0:
        d=int(n%b)
        if d<10:
            output+=str(d)
        else:
            output+=chr(ord("a")+d-10)
        n//=b
    output= output[::-1]
    return output
inum=int(input())
ibase=int(input())
ans=fun1(inum,ibase)
Counter=0
for i in range(len(ans)-1):
    if ans[i]=='0' and ans[i+1]=='0':
        Counter+=1
if Counter==0:
    print(-1)
else:
    print(Counter)
