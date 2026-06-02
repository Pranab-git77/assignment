i=int(input("Enter the number of angles: "))
ang = []
for j in range(i):
    a = int(input("Enter angle: "))
    ang.append(a)

def valid_angle(x):
    if x >= 0 and x <= 180:
        return True
    else:
        return False
    
valid = list(filter(valid_angle, ang))
print(valid)

def servo(x):
    return x*10
sa = list(map(servo, valid))
print(sa)