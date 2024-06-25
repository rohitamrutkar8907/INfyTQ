list1=[]

rs=0
n=int(input())
for i in range(n):
    ele=int(input())
    list1.append(ele)
val=int(input("Ener trishold value:"))
for i in list1:
    if i<=val:
        rs+=1
    else:
        rs=rs+2
    
print("Rupes to pay Airport:",rs)
