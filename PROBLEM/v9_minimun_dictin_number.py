n=int(input())
list_num=list(map(int,input().split("")))
list_count=[]
unique=set(list_num)
for i in unique:
    count=list_num.count(i)
    list_count.append(count)
list_count.sort()
len=len(list_count)
for count in list_count:
    if(count<=n):
        n-=count
        len-=1
    else:
        break
print(len)

"""
RESULT:
4  
1 1 1 2 2 3 3 4 5 6
3
"""