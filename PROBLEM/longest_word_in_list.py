str=input()
words=str.split()
final_list=[]

for word in words:
    final_list.append((len(word),word))

final_list.sort()
print(final_list[-1][1])

"""result
maruti mercediz bmw tata hundai
mercediz
"""