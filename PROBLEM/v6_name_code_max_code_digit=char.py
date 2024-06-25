#take input name and code and check max digit in code pritn the char=maxno if not then print x
#rohit:2,amrutkar:4,rudra:8
#oux

input_str=input()
ele=[]
final_str=""
ele=input_str.split(",")
for i in ele:
    sub_ele=i.split(":")
    name=sub_ele[0]
    number=sub_ele[1]
    name_lenth=len(name)

    max=0

    for digit in number:
        if(int(digit)<=name_lenth):
            if(max<int(digit)):
                max=int(digit)
    if(max==0):
        final_str+="x"
    else:
        final_str+=name[max-1]
print(final_str)