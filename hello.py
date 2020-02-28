"""
n1,n2,n3 = input('Enter 3 numbers :- ').split(',')
avg = (int(n1) + int(n2) + int(n3)) / 3
print(f'The average is {avg}')
print('The average is {}'.format(avg))


n1 = int(input('Enter number 1 :- '))
n2 = int(input('Enter number 2 :- '))
sum = n1 + n2
print('Total is ' + str(sum))
name, age = input('Enter your name and age ').split(',')
print('Hello ' + name + ' Your age is ' + str(age))
print('Hello {} your age is {}' .format(name, age))
print(f'Hello {name} your age is {age}')
"""
"""
name, char = input('Enter your name :- ').split(',')
lowername = name.lower()
lowerchar = char.lower()
print(f'lenth of your name is {str(len(name))}')
print(f'{char} is {lowername.count(lowerchar)} times in string {name}')
"""
"""
age = int(input('Enter your age:-'))
if age >= 14:
    print('You are above 14 years')
else:
    print('Sorry you are under 14')    
"""
"""
num = 7
gnum = int(input("Enter any number between 1 to 10 :-"))
if num == gnum:
    print("You Won this game:)")
else:
    if gnum > num:
        print("Too high") 
    else:
        print("Too lowest")  
"""
"""
age = int(input("Enter your age :-"))
name =  input("Enter your name:-")
name = name.lower()
name = name.replace(' ' , '')
if age >= 10 and name[0] == "a":
    print("You Can watch coco movie!!")
else:
    print("You can not watch this movie!")    
"""
"""
age = input('Enter your Age :-')
age = int(age)
if age == 0 or age < 0:
    print('Invalid Input!')
elif 0<age<4:
    print('Ticket Price:- Free')
elif 3<age<11:
    print('Ticket price:- 150')
elif 10<age<61:
    print('Ticket Price:- 250')
else:
    print('Ticket Price:- 200')                
"""
"""
num = int(input('Enter any number:-'))
sum = 0
i = 1
while i <= 10: 
    print(f'{num} * {i} = {num * i}')  
    sum = sum + i
    i = i + 1

print(f'The sum is {sum}')    
"""
"""
n = input('Enter any number :-')
sum = 0
i = 0
while i < len(n):
    sum = sum + int(n[i])
    i = i + 1
print(f'The sum is {sum}')    
"""
"""
name = input('Enter your name :-')
i = 0
tmp = ''
while i < len(name):
    if name[i] not in tmp:
        print(f'{name[i]} : {name.count(name[i])}')
        tmp += name[i]
    i += 1 
"""
"""    
for i in range(10): #0 to 9
    print(f'Hello world {i}')
"""
"""   
num = int(input("Enter a number:-"))
sum = 0
for i in range(1, num + 1):
    sum += i
print(sum) 
"""
"""
num = input("Enter a number:-")
sum = 0
for i in range(len(num)):
    sum += int(num[i])
print(sum)
"""
"""
name = input("Enter your name :-")
tmp = ""
for i in range(len(name)):   
    if name[i] not in tmp:
        print(f"{name[i]} : {name.count(name[i])}")
        tmp += name[i]
"""
"""
for i in range(1,11):
    print(i)
    if i == 5:
        break        
for i in range(1,11):
    if i == 5:    
        continue
    print(i)
"""
"""
import random
num = int(input("Enter a number between 1 to 10:-"))
wnum = random.randint(1,10)
guess = 1
game_over = False
while not game_over:
    if num == wnum:
        if guess == 1:
            print(f"You Win this game in first time :)")
            game_over = True
        else:    
            print(f"You Win this game in {guess} times :)")
            game_over = True
    else:
        if wnum < num:
            print("Too High :(")
            num = int(input("Guess Again:-"))
            guess += 1             
        else :
            print("Too low :(") 
            num = int(input("Guess Again:-"))
            guess += 1   
"""
"""
for i in range(2,11,2):
    print(i) 
"""
"""
for i in range(10,0,-1):
    print(i)
"""
"""
num = input("Enter a number")
sum = 0
for i in num:
    sum += int(i)
print(sum) 
""" 
"""
 # functions
def add(a,b):
    return a + b
print(add(5,5))
"""
"""
# find last character of word
def lchar():
    name = input("Enter your name :-")
    return name[-1]
l_char = lchar()
print(l_char)    
"""
"""
def highnumber():
    a = int(input("Enter first number :-"))
    b = int(input("Enter second number :-"))
    c = int(input("Enter third number :-"))
    if a > b and a > c:
        print("A is max")
    elif b > a and b > c:
        print("B is max")
    else:
        print("C is max")        
highnumber()                
"""
"""
def ispalindrom():
    name = input("Enter any word :-")
    tmp = name        
    rev = name[::-1]
    if tmp == rev:
        print("Number is palindrom")
    else:
        print("Number is not palindrom")            
ispalindrom()
"""
"""
def fibonacci():
    num = int(input("Enter a number for fibonacci series :-"))
    a = 0
    b = 1
    if num == 1:
        print(a)
    elif num == 2:
        print(a,b)
    else:
        print(a,b, end = " ") 
        for i in range(num - 2):
            c = a + b
            a = b
            b = c 
            print(c, end = " ")  
fibonacci()                                    
"""
"""
def sqr(a):
    square = []
    for i in l:
        square.append(i**2)
    return square
l = list(range(1,11))  
print(sqr(l))
"""
"""
ls = list(range(1,11)) 
def rev(l):
    revls = []    
    for i in range(len(l)):
        pop_item = l.pop()
        revls.append(pop_item)     
    return revls
print(rev(ls))   
"""
"""
ls = ['cba', 'fed', 'ihg']
def rv(l):
    for i in range(len(l)):
        l[i] = l[i][::-1]
    print(l)
    return
rv(ls) 
""" 
""" 
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 18, 24, 29, 43, 44, 12]
def oddeven(l):
    odd_even = []
    odd = []
    even = []    
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i) 
    odd_even = [odd, even]
    print(odd_even)
    return
oddeven(ls)   
""" 
""" 
def commen(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    print(output)    
    return
commen([1,2,5,7], [5,6,7,9])    
"""
""" 
# Min and Max function
ls = [2,40,24]
print(min(ls))
print(max(ls))
"""
"""
ls = [1, 2, 3, [4,5,6], [7,8,9] ]
def check(l):
    cnt = 0
    for i in l:
        if type(i) == list:
            cnt += 1 
    print(cnt) 
    return           
check(ls) 
"""
"""
def udf():
    print("")
    flag = 1
    while flag == 1:
        print("Press 1 for Sum,\nPress 2 for Multiplication,\nPress 3 for Substraction,\nPress 4 for devision;\nPress 0 to Exit();")
        f = int(input("Which function are you want to use?:-    "))
        if f == 0:
            flag = 0
            break        
        if f != 1 and f != 2 and f != 3 and f != 4:
            print("Please Enter valid Input!!!")
        else:            
            a = int(input("Enter Number 1:-     "))
            b = int(input("Enter Number 2:-     "))                        
            if f == 1:
                print(f"Sum is {a + b}")
            elif f == 2:
                print(f"Multiplication is {a * b}")  
            elif f == 3:
                print(f"Substraction is {a - b}")
            elif f == 4:
                print(f"Devision is {a / b}")
        d = input("Are you want to repeat this Function:(y / n):    ")
        if d == "y":
            pass
        elif d == "n":
            flag = 0
        else:
            while flag == 1:
                print("Enter valid Input!!") 
                d = input("Are you want to repeat this Function:(y / n):  ") 
                if d == "y":
                    break
                elif d == "n":
                    flag = 0  
                else:
                    pass                                                          
udf()             
"""
'''
#Tuples Examples

tp = (1,2,3,4,5,6.0)
for i in tp:
    print(i)

num = (1)
num2 = (1,)
ex = 'Husen', 'Smeet', 'Bhargav', 'Hardik'
print(type(num))
print(type(num2))
print(type(ex))

# Tuple unpacking
employee = ('Husen', 'Hardik', 'Smit')
em1, em2, em3 = employee
print(f'{em1}, {em2}, {em3}')

# ḷist inside tuples
tp = ('abc', ['def', 'ghi'])
print(tp)
tp[1].pop()
print(tp)
tp[1].append('abcd')
print(tp)

# min, max, sum,
num = (5,6,4,2)
print(min(num))
print(max(num))
print(sum(num))

# Fucntion returning two values
def fun(int1, int2):
    add = int1 + int2
    mul = int1 * int2
    return add, mul
sum, mul = fun(5,6)
print(sum)
print(mul)
'''
# Dictionary Intro
# user = {'name' : 'Husen', 'lname' : 'Lokhandwala'}
# print(user);
# second method to create Dictionary
# user = dict(name = 'Husen', lname = 'Lokhandwala')
# print(f"Hello {user['name']} {user['lname']} how are you:)")


# # Adding key and values in empty Dictionary
# user = {}
# user['name'] = 'Husen'
# user['lname'] = 'Lokhandwala'
# print(user)

# user = {
#     'name' : 'Husen',
#     'lname' : 'Lokhandwala',
#     'age' : 20,
#     'stream' : 'BCA'
# }

# Check if key is exist in dictionary

# if 'name' in user:
#     print('Yes')

# check if value exist in dictionary using values() method

# if 'Husen' in user.values():
#     print('Yes')
# else:
#     print('No')

# Loop in Dictionary
# for i in user.values():
#     print(i)

# print(user.items())

# How to add data in dictionary
# user['fav_color'] = 'red'
# print(user)

# Pop method
# print(f'Returned value ', user.pop('stream'))
# print(user)

# popitem method
# user.popitem()
# print(user)


# Update Method 
# user = {
#     'name' : 'Husen',
#     'lname' : 'Lokhandwala',
#     'age' : 20,
#     'stream' : 'BCA'
# }
# more_info = {
#     'name' : 'Husain',
#     'fav_subject' : 'Python'
# }
# user.update(more_info)
# print(user)


# fromkeys method for dictionary
# clear method
# get method


# exercise cube finder
# cube = {}
# n = int(input("Enter number :- "))
# for i in range(1, n+1):
#     cube[i] = i*i*i
# print(cube)


# exercise 2

'''

class myClass:
    __a = 0

    def count(self):
        self.__a += 1
o = myClass()
print(o._myClass__a)
o.count()
print(o._myClass__a)
o.count()
print(o._myClass__a)
o.count()
print(o._myClass__a)

'''
'''

class myClass:
    def __init__(self):
        self.a = 123
        self._b = 123
        self.__c = 123

o = myClass()
print(o.a) 
print(o._b)
print(o._myClass__c)     

'''


'''
class myClass:
    def __init__(self):
        self.__version = 22

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version

o = myClass()
o.getVersion()
o.setVersion(23)
o.getVersion()
print(o._myClass__version)        
'''

# def search(values, no):
#     search_at = 0
#     search_res = False

#     while search_at < len(values) and search_res is False:
#         if values[search_at] == no:
#             search_res = True
#         else:
#             search_at += 1
#     return search_res

# l = [12, 98, 65, 12, 77, 45, 82]

# print(search(l, 12))
# print(search(l, 45))
# print(search(l, 78))

import pylab
pylab.figure(1)
pylab.plot([1,2,3,4,5],[1,7,3,5,12])
pylab.show()