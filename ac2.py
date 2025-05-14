def pal(t):
    e=len(t)-1
    s=0
    while(s<e):
        if t[s]!=t[e]:
            return False
        s=s+1
        e=e-1
    return True
tup=(4,7,8,3)
if pal(tup):
    print("Palendrome")
else:
    print("not palendrome")