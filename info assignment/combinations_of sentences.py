sentences=[]
def combbination(subject,verb,object):
    for i in subject:
        for j in verb:
            for k in object:
                sentences.append(i+' '+j+' '+k+' ')
    return sentences        
a=['I','YOU']
b=['PLAY','LOVE']
c=['cricket','chess']
print(combbination(a,b,c))