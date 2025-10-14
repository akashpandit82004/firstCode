# print("hello",end="$")
# print("morning")
# print("hello",10,20,20.14,"morning",sep="*")

import keyword
print(keyword.kwlist)

# a=4
# b=a
# print(b)

# num1=100
# num2=400
# print(num1,num2)
# num2=num1
# num1=500
# print(num1,num2)
# a=4+8+8
# print(a)
# a=40
# print(a)
# a=a+40
# print(a)


# a=b=c=40
# print(a,b,c)

# c="154"
# print(isinstance(c,str))
# print(isinstance('20',int))
# num1=40
# num2=40.5
# num3=num1+num2
# print(type(num3))

# a="great"
# print(list(a))
# s='gerr'
# print(str(s))

# name=input()
# print("good morning",name)
# print(2**3**2)
# 2**9
# ac=input("enter  AC/NON-AC")
# food=input("enter  veg/non-veg")
# if ac=="AC":
#     if food=="veg":
#         print("AC veg")
#     else:
#         print("AC non veg")
# else:
#     if food=="veg":
#         print("non- ac veg")
#     else:
#         print("non AC non-veg")
# a=10
# if a>3:
#     print(a)
    
# print("done")

#short hand
# drink=input("coffe/tea")
# if drink=="coffe":
#     print("coffe")
# else:
#     print("tea")

# **** short hand
# drink=input("coffe/tea")
# print("coffe") if drink=="coffe"else print("tea")
# a=10
# b=a        
# if a>b:
#       pass
#       print("done")
# a=0
# while a<5:
#     print(a)
#     a+=1

# a="akash"
# for i in a:
#     print(i)
# 
# for i in range(1,10,2):
#     print(i)
                
# a=[0,1,2]
# b=[3,4,5]  
# for i in a:
#     for j in b:
#         print(i,j) 
#nested list 
# /****************
#  print(lst.count("red"))
# print(lst.index("red"))
# lst = ["red","black","green","blue"]
# lst2 = lst.copy()
# lst.sort() #default ascending order
# lst.sort(reverse = True) #descending order
# lst.reverse()
# lst[::-1]
# lst.clear() #clear vs del
# del lst
# lst = ["red","black","green","blue","red"]
# lst.append("white")
# lst.extend(["yellow","orange"])
# lst.insert(2,"purple")
# lst.remove("red")
# lst.pop()
# lst.pop(2)

# print(lst)
##type casting
# a = 10 
# print(type(a))
# b = float(a)
# print(type(b))
# print(b)
#user input 
# name = chr(input("enter your name"))
# print(name)
# # print(type(name))
i = 10  #starting point
# while i >=0 :
#     print(i)
#     i-=1 #increment
# char = input("enter a character")
# if char== a or char == e or char == i or char == o or char == u:
# if char.islower():
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#         print("vowel")
#     else:
#         print("consonant")
# else:
#     print("not a alphabet")
# s=input("enter the number")
# principle_amount=50000
# time=3
# interest_amount=3
# total_interset=(principle_amount*time*time)/100
# print("total simple interset",total_interset)

# Take string input
user_input = input("Enter a string: ")

# Initialize counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Loop through each character
for ch in user_input:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1
    else:
        special_count += 1

# Print results
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Digits:", digit_count)
print("Special characters:", special_count)
