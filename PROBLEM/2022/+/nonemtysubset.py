def findNonEmptySubset(arr, N):
    mp = {}
    Sum = 0
    for i in range(N):
        Sum = (Sum + arr[i]) % N 
        if (Sum == 0) :
            print(i + 1)
            for j in range(i + 1):
                print(j + 1, end = " ") 
            return
            if Sum in mp :
                print((i - mp[Sum]))
                for j in range(mp[Sum] + 1,i + 1):
                    print(j + 1, end = " ")
            else:
                mp[Sum] = i 

# Driver code 

arr = [2, 3, 7, 1, 9] 

N = len(arr) 

findNonEmptySubset(arr, N)