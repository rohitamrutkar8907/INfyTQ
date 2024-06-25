
num=input()
len_of_number=len(num)
otp=""
for i in range(1,len_of_number,2):
    odd=int(num[i])
    odd=odd**2
    otp+=str(odd)

print(otp[:4])

'''
#it print even number square otp 

num=input()
lenl=len(num)
otp=""
for i in range(0,lenl):
    if int(num[i])%2==0:
        odd=int(num[i])
        odd=odd**2
        otp+=str(odd)

print(otp[:4])
'''