def myfun(input):
    stack=[]
    c=0
    for ele in input:
        if(ele=="[" or ele=="{" or ele=="(" ):
            stack.append(ele)
            c+=1
            continue
        if  len(stack)==0:
            return c+1
        temp=stack.pop()
        if(ele=="]" and temp=="["):
            c+=1
        elif(ele=="}" and temp=="{"):
            c+=1
        elif(ele==")" and temp=="("):
            c+=1
        else:
            return 0
    if  len(stack)==0:
        return 0
    else:
        return c+1

a=input()
res=myfun(a)
print(res)