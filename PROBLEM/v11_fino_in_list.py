#it print list of fabnacci in arry with max no
"""
2,3,5,8,9,10,11
4
"""

input_arr=list(map(int,input().split(",")))
input_arr.sort()
max_num=max(input_arr)
num=0
num2=1
fib_list=[]
fib_list.append(num)
fib_list.append(num2)

while(num2<max_num):
    sum=num+num2
    num=num2
    num2=sum
    fib_list.append(num2)
fib_ser=[]
for i in range(len(input_arr)):
    if input_arr[i] in fib_list:
        fib_ser.append(input_arr[i])
        
if len(fib_ser)>2:
    print(len(fib_ser))
else:
    print(-1)
