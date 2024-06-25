"""
num+reverse(num)=is palindromthen(9339) then it return
else sum+reverse(sum)=plaindron the it return if it is
"""


def rev(num):
    return int(str(num)[::-1])
     

def ispalindrom(num):
   return str(num)[::-1]==str(num)


num=int(input())
while True:
    num=num+rev(num)
    if ispalindrom(num):
        print(num)
        break



