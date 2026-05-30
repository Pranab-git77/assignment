
import matplotlib.pyplot as e
import random as r

l = [9, 5, 6, 1, 2, 4, 8, 7, 3]
pas=[l.index(n) for n in range(1,len(l))]


if len(l) <= 1:
    print("not valid")

else:
    o=0
    while o<len(l)-1:
        co=0
        for n in range(0,len(l)):
            if l[o]>l[n]:
                co+=1
        if o<8:
            o+=1
        l[co],l[o]=l[o],l[co]
        print(o)
print(l)


