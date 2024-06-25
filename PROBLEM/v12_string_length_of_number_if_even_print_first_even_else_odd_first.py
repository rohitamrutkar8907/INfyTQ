"""
TAKE INPUT STRING AND PRINT NUMBER IN STRING
IF LENGTH OF special ch NUMBER IS EVEN THE PRINT 1ST EVEN NUMBER AND THEN ODD NUM IN SERIES
IF LENGTH OF  special ch NUMBER IS ODD THE PRINT 1ST ODD NUMBER AND THEN EVEN NUM IN SERIES

RESULT:
A5C67R21I@P#8T
652781



"""


myinput=input()
even,odd=[],[]
spch=0
for a in myinput:
    if not(a.isalnum()):
        spch+=1
    if a.isdigit():
        if int(a)%2==0:
            even.append(a)
        else:
            odd.append(a)

for b in range(max(len(even),len(odd))):
    if b<len(even):
        print(even[b],end="")
    if b<len(odd):
        print(odd[b],end="")
        