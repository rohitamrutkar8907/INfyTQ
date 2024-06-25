#take input name and code 
# then sq digit in code
# adding of sq 
# if sum is even 
# last 2char on beginig
# if sum is odd 
# then first 1char on last 
'''
abcd:1234,kjhgf:3445,iuyt:8765
cdab gfkjh ytiu
 '''

string=input()
str_list=string.split(",")
result=""
for i in str_list:
    string,number=i.split(":")
    length=len(string)
    sum=0
    for digit in number:
        sum+=(int(digit)**2)
    if(sum%2==0):
        sub=string[length-2:length]
        result=sub+string[0:length-2]
    else:
        sub=string[0]
        result=string[1:length]+sub
    print(result,end=" ")