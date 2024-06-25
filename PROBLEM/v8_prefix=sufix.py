"""
RESULT
abcdabc
3
"""

str=input()
length=len(str)
mid=length//2
for i in range(mid,0,-1):
    prefix=str[0:i]
    suffix=str[length-i:length]
    if(prefix==suffix):
        print(len(prefix))
        break