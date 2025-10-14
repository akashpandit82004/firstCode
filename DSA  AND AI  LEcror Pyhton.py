#create A frozen set
st=frozenset([1,2,3])
print(st)
st=frozenset("hello")
print(st)
#hasable
dt={
    frozenset([1,2]):"pair",
    frozenset([3,4]):"hello" 
}
print(dt)
# #accessing
# print(dt[frozenset([3,4])])
print(type(dt))


#while loop
#a loop that execute a block of code repeatedly as long as 
#a condition is true
#it is called an entry  controlled  loop(condition checked)
#befor exucution
# example
# i=0#starting point
# while i<10:
#     print(i)
#     i+=1#increment
    
    # reversed
# i=10
# while i>10:
#     print(i)
#     i-=10
    
    #break
# i=0
# while i<10:
#         if i==5:
#              break
#         print(i)
#         i+=1

#contiuue
# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     print(i)
    
 # Question1
#  print the multiplication tabel of 5 using while loop
# n=int(input("enter the number"))
# i=1
# while i<=10:
#     print(f"{n}X{i}={n*i}")
#     i+=1



    

 
    
  
           
           
        
    
