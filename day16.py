number= int(input("enter the number"))
print(number)
match number:
 
     
       case 1:
           print("one")
       case 2:
           print("two")
       case 3:
           print("three")
       case 4:
           print("four")
       case _ if number != 90:
           print("is no a 90",number)
    
       case _ if number !=80:
           print(number,"number is 80")
       case _:
           print(number)
                      
    
           
           
            
            
       

        
            
          
        
        