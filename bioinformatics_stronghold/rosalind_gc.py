dic = {}
with open('rosalind_gc.txt','r') as fp:
    for line in fp:
        if line.startswith('>'):
            key = line.replace('>','').strip()
            dic[key] = ''
        else:
            dic[key] += line.strip()

perc = {}
for key, value in dic.items():
    perc[key] = ((value.count('C')+value.count('G'))/len(value))*100.0 # probably can be optimized

print(perc)

perc = {value:key for key, value in perc.items()}
print(perc[max(perc)])
print(max(perc))






