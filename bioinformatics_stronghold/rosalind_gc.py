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

'''
e = max(dna.items(), key=gc_content)

Even max function can have a key, this means that each item in the list is being passed to a function gc_content, which is defined by the user.

Another 2.7 sol:
----------------

dnafile = open('rosalind_gc.txt', 'r')
raw = dnafile.read() # reads in the entire file, I guess
d = {}
for seqblock in raw.split(">")[1:]:
    parts = seqblock.split("\n")
    fasta = parts[0]
    seq = ''.join(parts[1:])
    gc = 100 * ( seq.count("G") + seq.count("C") ) / float(len(seq))
    d[gc] = fasta
print d[max(d)], max(d)

'''





