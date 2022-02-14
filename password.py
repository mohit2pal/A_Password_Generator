import random

# trunk-ignore(flake8/W605)
x = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyl][\][\]\;./0123456789"

passnew = ""

y = int(input("Enter the length of the password"))

for i in range(y):
    passnew = passnew + random.choice(x)

print("The generated password is ", passnew)
