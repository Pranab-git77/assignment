x = int(input("Enter first number: "))
y  = int(input("Enter second number: "))

s = min(x, y)

for i in range(1, s + 1):
    if x % i == 0 and y % i == 0:
        gcd = i

lcm = (x * y) // gcd

print("GCD =", gcd)
print("LCM =", lcm)