from typing import Counter
n=[2,26,4,25,78,21]
li=[]
c=[]
for i in n:
    ele=i%6
    li.append(ele)
c=li.count(li)
re=Counter(li)
print(re)
print(li)