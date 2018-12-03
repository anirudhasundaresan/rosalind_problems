str_ = []

with open('rosalind_subs.txt', 'r') as fp:
    for line in fp:
        str_.append(line.strip())

line = str_[0]
check = str_[1]

ind_ = ''

for ind in range(len(line)):
    if line[ind:].startswith(check):
        ind_ += str(ind+1) + ' '

print(ind_)

'''
Another solution using find function:

dnaSeq = "GATATATGCATATACTT"
subSeq = "ATAT"

r = 0
while r != -1 :
        r = dnaSeq.find(subSeq,r+1)
        print r+1

https://www.programiz.com/python-programming/methods/string/find
https://www.geeksforgeeks.org/string-find-python/
'''

