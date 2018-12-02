skip = 0
with open('rosalind_ini5.txt','r') as fp:
    for line in fp:
        if skip!=0:
            print(line)
            skip = 0
        else:
            skip = 1
