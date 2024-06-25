'''in_stack=[]
Stack=[]
def modify_stack (in_stack):
    if in_stack.is_empty():
        return

    temp_stack =Stack(in_stack.get_max_size())

    number = 1

    while (not in_stack.is_empty()):

        temp_stack.push(in_stack.pop() *number)
        number +=1

        temp_stack.push (temp_stack.pop () +temp_stack.pop())
        return temp_stack'''
       
'''
input_list=[33,15,27,8,35,42,19,48]
def selection_sort(input_list):
    size=len(input_list)
    for num in range (0, size-1):
        min_value_index = num

        for val in range (num+1, size):
             if input_list [val] <input_list [min_value_index]:
                  min_value_index = val

        if min_value_index != num:
            temp = input_list [num]

        input_list [num] = input_list [min_value_index]
        input_list [min_value_index] = temp
        return input_list'''

n = input()

t =int(input())
l=[n]
for _ in range(t-1):
    s=""
    n = l[-1]
    prev = n[0]
    c = 1
    for i in range(1, len(n)):
        if(prev != n[i]):
            s+= (str(c)+""+str(prev))
            prev = n[i]
            c=1
        else:
            c +=1
s += (str (c)+""+str(prev))
l.append(s)
print(*l, sep=",")