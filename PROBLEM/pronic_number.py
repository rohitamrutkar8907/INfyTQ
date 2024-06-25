"""
Pronic number = 1*2=2 2*3=6
12345
2,12
"""
lst=[]
for i in range(1,1000):
    lst.append(i*(i+1))

mystr=input()
myset=set()

for i in range(len(mystr)):
    s1=" "
    for j in range(i,len(mystr)):
        s1 += mystr[j]
        if (int(s1)) in lst:
            myset.add(int(s1))

myset=sorted(list(myset))
if(len(myset)!=0):
    for i in range(len(myset)-1):
        print(myset[i],end=",")
    print(myset[len(myset)-1])
else:
    print(-1)