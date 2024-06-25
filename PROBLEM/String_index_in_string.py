"""result
rohitamrutkar
hi ru
{'hi': [2, 3], 'ru': [7, 8]}"""


str=input()
check_list=[i for i in input().split()]
res=dict()
for ele in check_list:
    if ele in str:
        start_index=str.index(ele)
        res[ele]=[start_index,start_index+len(ele)-1]

print(res)