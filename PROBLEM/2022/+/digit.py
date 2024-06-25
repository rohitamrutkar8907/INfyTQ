def check(s):
    for i in s:
        if not(i.isalpha() or i.isdigit() or i=="+" or i=='/'):
            return 1
    return 0

def solve(s):
    if(check(s)):
        return -1
    st=""
    for i in s:
        c=str(bin(ord(i))[2:])
        for j in range(8-len(c)):
            c="0"+c
        st+=c
            
    n=6

    l=[st[i:i+n] for i in range(0,len(st),n)]
    x=len(l[-1])
    for i in range(6-x):
        l[-1]+='0'
    ans=[]
    for i in l:
        ans.append(int(i,2))
    answer=""
    for i in ans:
        if(i==62):
            answer+='+'
        elif(i==63):
            answer+='/'
        elif(i<26):
            answer+=chr(65+i)
        elif(i<52):
            answer+=chr(71+i)
        else:
            answer+=chr(i-4)
    return answer
           
       


s=input()
print(solve(s))