str=input()
x=input()
indixes=[]
for idx,ele in enumerate(str):
    if ele==x:
        indixes.append(idx)
ree=indixes[len(indixes)//2]
print(ree)

"""
rohit amrutkar
r
8
"""