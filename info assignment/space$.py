def solve(instr):
    freqLetter = {}
    freqDigit = {}
    for ch in instr:
        if((ord(ch)>=65 and ord(ch)<= 90) or ( ord(ch)>=97 and ord(ch)<=122)):
            if ch in freqLetter:
                freqLetter[ch] += 1
            elif ch!=' ':
                freqLetter[ch] = 1
        elif(ord(ch)>=48 and ord(ch)<=57):
            if ch in freqDigit:
                freqDigit[ch] += 1
            elif ch!=' ':
                freqDigit[ch] = 1
    letter,digit = 0,0
    for k,v in freqLetter.items():
        letter = max(letter,v)
    
    for k,v in freqDigit.items():
        digit = max(digit,v)
        
    index = abs(letter-digit)
    ch = instr[index]
    
    res = ""
    if ch!=' ':
        for i in instr:
            if i!=ch and i !=' ':
                res += i
            if i == " ":
                res += "$"
    else:
        for i in instr:
            if i ==' ':
                res += "$"
            else:
                res += i

    return res

if __name__ == "__main__":
    instr = input()
    print(solve(instr))
