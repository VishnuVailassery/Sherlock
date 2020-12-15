from math import *


def prime(a):
    for i in range(2, floor(sqrt(a) + 1)):
        if a%i == 0:
            return False

    else:
        return True

n=int(input("enetr num"))

x=len(str(n))
cost=0
for i in range(x):
    fd=n//(10**(x-1))

    n=((n*10)+fd)-(fd*(10**(x)))
    print(n)

    if prime(n):
        cost=cost+n



print("cost is",cost)

for i in range(x):
    fd=n//(10**(x-1))

    n=((n*10)+fd)-(fd*(10**(x)))
    print(n)

    if prime(n):
        cost=cost+n