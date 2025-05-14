w=(0,1,1,1,0,1,0)
s=0
r=0
for day in range(0,7):
    if w[day]==0:
        r=r+1
    else:
        s=s+1


if s>r:
    print("Great weather.go for mountain hikes")
else:
    print("Bad weather.not recommended for mountain hikes")