#abcabc
import string
string=input()
length=len(string)
unique=''
for i in range(length):
    sub_str=string[i]
    for j in range(i+1,length):
        sub_str+=string[j]
        sunl=len(sub_str)
        if sunl>=3 and len(set(sub_str))==sunl:
            if(len(unique)<sunl):
                unique=sub_str
if(len(unique)==0):
    print("-1")
else:
    print(unique)