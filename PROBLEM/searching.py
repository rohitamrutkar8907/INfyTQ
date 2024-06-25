'''
def linearsearching(a,size,element):
    for i in range(0,size):
        if(a[i]==element):
            return i
    
    return -1

a=[1,5,6,8,7,9]
size=len(a)
element=6
searchindex=linearsearching(a,size,element)
print(f"element is {element} found at {searchindex}")
'''

def binarysearching(a,size,element):
    high=size-1
    low=0
    while(low<=high):
        mid=int((high+low)/2)
        if(a[mid]==element):
            return mid
        if(mid<element):
            low=mid+1
        else:
            high=mid-1
    return -1        
a=[1,5,6,8,7,9]
size=len(a)
element=6
searchindex=binarysearching(a,size,element)
print(f"element is {element} found at {searchindex}")

print(len(a))