#identify the pair in two input that can swap no fron both input and sum of both are equal
"""
9 2 4 14 5 1 3
1 12 7 9 2 3
4,2,14,12,9,7,5,3,3,1
"""

input1=list(map(int,input().split()))
input2=list(map(int,input().split()))
s1=sum(input1)
s2=sum(input2)
output=[]
list1=[]
for i in input1:
    for j in input2:
        if s1-i+j==s2+i-j:
            output.append((i,j))

for i,j in output:
    if i*j%2==0:
        list1.append(i)
        list1.append(j)
        

for i,j in output:
    if (i*j)%2!=0:
        list1.append(i)
        list1.append(j)

if len(list1)!=0:
    for i in range(len(list1)-1):
        print(list1[i],end=",")
    print(list1[len(list1)-1])
else:
    print(-1)


"""
9 2 4 14 5 1 3
1 12 7 9 2 3
"""
