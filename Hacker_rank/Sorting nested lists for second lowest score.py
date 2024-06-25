list1=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
list2=sorted(list(set([i[1] for i in list1])))
a=list2[1]
list3=[i for i in list1 if i[1]==a]

list3.sort()

for i in list3:
    print(i[0])