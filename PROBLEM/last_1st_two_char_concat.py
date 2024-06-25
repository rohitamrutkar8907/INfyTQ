"""
result:
pyhon
pyon
print first n last two char of string
"""
string=input()
if(len(string)<2):
    print("empty string")
else:
    print(string[0:2]+string[-2:])

#second method

"""
string=input()
length=len(string)

if(length<2):
    print("empty string")
else:
    a=slice(0,2)
    b=slice(length-2,length)
    print(string[a]+string[b])

"""
