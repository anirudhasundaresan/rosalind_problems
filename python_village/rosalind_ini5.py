skip = 0
with open('rosalind_ini5.txt','r') as fp:
    for line in fp:
        if skip!=0:
            print(line)
            skip = 0
        else:
            skip = 1


'''
(better solution : more pythonic)
with open('poem.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 2 == 0:
            print(line)
'''

