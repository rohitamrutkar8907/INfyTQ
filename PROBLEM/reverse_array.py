'''lis=[]
def a():
    n=int(input("enter size "))
    for i in range(n):
        ele=int(input("enter element "))
        lis.append(ele)
t=int(input("case  "))
while t!=0:
    a()
    t-=1    
print(lis[::-1])'''

t=int(input())
while t!=0:
    n=int(input())
    li=list(input())
    t-=1 
li.reverse()
listToStr = ''.join([str(i) for i in li])
print(listToStr)