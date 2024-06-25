import re
str=input()
digit=[i for i in set(str) if i.isdigit()]
digit.sort()
digit.reverse()
num=int(''.join(digit))
if num%2==0:
    print(num)
else:
    length=len(digit)
    for i in range(length-1,0,-1):
        if int(digit[i])%2==0:
            a=digit[i]
            digit.remove(a)
            digit.insert(length-1,a)
            even=int(''.join(digit))
            print(even)
            break
    else:
        print(-1)




"""
num=input("Enter a number:")
num=list(set(num))
x=[]
for i in num:
    if i.isdigit():
        x.append(int(i))
x.sort()
x=x[::-1]
print(x)
sum=0
a=0
flag=0
for i in x:
    sum=sum*10+int(i)
if sum%2==0:
    print(sum)
else :
    for i in range(len(x)-1,0,-1):
        if int(x[i])%2==0:
            a=x[i]
            x=x[:i]+x[i+1:]
            flag=1
            break
    x.append(a)
    sum=0
    if flag==1:
        for i in x:
            sum=sum*10+int(i)
        print(sum)
    else:
        print(-1)
"""