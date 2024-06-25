from string import ascii_lowercase, ascii_uppercase
from sys import set_coroutine_origin_tracking_depth


result=[0]*2
def lower_upeeer_find(sentence):
    for  i  in  sentence:
        if i in ascii_uppercase:
            result[0]+=1
        if i in ascii_lowercase:
            result[1]+=1
        
    return result
a="RohitAmRutkar"
print(lower_upeeer_find(a))
