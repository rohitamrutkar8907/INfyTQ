str=input()
n=int(input())
x=input()
output=""
for index,letter in enumerate(str):
    if index%n==0 and index!=0:
        output=output+x
    else:
        output=output+ letter
print(output)


'''
output
rohitamrutkar
5
#
rohit#mrut#ar'''
