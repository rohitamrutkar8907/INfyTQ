def ispalindrom(n):
    s=str(n)
    return s==s[::-1]

def find_num1(innum):
    innum-=1
    while True:
        if ispalindrom(innum):
            return innum
        innum-=1

def find_num2(innum):
    innum+=1
    while True:
        if ispalindrom(innum):
            return innum
        innum+=1
def chk(n):
    while n>0:
        b=find_num1(n)+find_num2(n)
        if ispalindrom(b):
            return b
        n-=1
innum=int(input())
print(chk(innum))