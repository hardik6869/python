import re
validation = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def validate(email):
    if re.search(validation,email):
        print(f"{email} is Valid")
    else:
        print(f"{email} is not Valid")

n = int(input("how many times you want to enter email :- "))
l = []
for i in range(n):
    tmp = input("Enter email :- ")
    l.append(tmp)
for j in l:
    validate(j)