a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

s = min(a, b)
for i in range(1, s + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)