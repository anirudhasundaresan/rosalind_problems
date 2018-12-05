a, b = 0, 1

def fibo(a, b, n, count):
    c = a+b
    a, b = b, c
    count += 1
    if count==n:
        print(c)
    else:
        fibo(a, b, n, count)

n = 23
count = 1
print(fibo(a, b, n, count))
