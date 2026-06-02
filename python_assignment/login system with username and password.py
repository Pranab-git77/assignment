c_u = "USERNAME"
c_p = "159753"

u = input("Enter username: ")
p = input("Enter password: ")

if u == c_u and p == c_p:
    print("Login Successful!")

elif u != c_u:
    print("Invalid Username!")

elif p != c_p:
    print("Invalid Password!")