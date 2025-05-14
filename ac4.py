def avgfun(n):
    l1=list(n)
    s=0
    for x in l1:
        s=s+x
    return s

n=(12,56,67,55,34)
print("Tuple:",n)
print("Average:",avgfun(n)/len(n))