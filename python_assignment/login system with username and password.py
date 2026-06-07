cu = "USERNAME"
cp = "159753"

u = input("Enter username: ")
p = input("Enter password: ")

if u == cu and p == cp:
    print("Login Successful!")

elif u != cu:
    print("Invalid Username!")

elif p != cp:
    print("Invalid Password!")