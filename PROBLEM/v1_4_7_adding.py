'''
#v1
1,2,3,4,5,6,7,8 
num1=1+2+3+8==14
num2=4567
output==4581
'''

string=input()
str_list=string.split(",")
len_of_str=len(str_list)

index_4=str_list.index("4")
index_7=str_list.index("7")

num1=0
num2=""

for i in range(0,len_of_str):
    if (i<index_4) or (i>index_7):
        num1+=int(str_list[i])

for i in range(index_4,index_7+1):
    num2+=str_list[i]

print(num1+int(num2))