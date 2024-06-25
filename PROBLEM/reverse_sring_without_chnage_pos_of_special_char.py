"""rohit#amrutkar
r a k t u # r m a t i h o r"""

import re
string=input()
alphabets=re.findall("[a-zA-Z]",string)
alphabets.reverse()
for i in range(len(string)):
    if not(string[i].isalpha()):
        alphabets.insert(i,string[i])
print(" ".join(alphabets))
