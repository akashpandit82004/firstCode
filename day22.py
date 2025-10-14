l=[1,2,3,"akash",True]
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

# ********************List index
# color=["apple","mango","banana","grapes"]
# print(color[0])
# ***********************negative index
# color=["apple","mango","banana","grapes"]
# print(color[-3])   # neagative index
# print(color[len(color)-3]) #positive index
# print(color[5-3])
# print(color[2])
# ****************************check weather  an item present in list
# if "6" in color:
#     print("yes")
# else:
#     print("no")
#     # same thing for applie for string as well as
#     if "arry" in "harry":
#         print("yes")
#         print(color[:])
        
        
 # ************************ list comprehension
list=[i*i for i in range(10)if i%2==0] 
print(i*i for i in range(10))
print(list)


        
        