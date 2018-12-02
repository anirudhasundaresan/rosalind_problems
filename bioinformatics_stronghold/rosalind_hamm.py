str = []
with open('rosalind_hamm.txt','r') as fp:
    for line in fp:
        str.append(line.strip())

line1 = str[0]
line2 = str[1]
count = 0

for fir, sec in zip(line1, line2):
    if fir!=sec:
        count += 1

print(count)

'''
Better solutions:
-----------------

print [ a!=b for (a, b) in zip(s1, s2)].count(True) # this is list comprehension, better than writing the same thing in 3 sentences and with an extra count.

Some people have done this using operator.ne and the map function.
sum(map(operator.ne, s1, s2))

https://docs.python.org/3/library/operator.html

sum([True, True]) --> 2
sum([True, False, True]) --> 2

True amounts to 1 and False amounts to 0.

'''

