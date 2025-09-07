sugar_amount = 2
print(f"initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")
 
# intialy sugar amount =2 tha but according to non-mutability if i changed the 
# value , the value of sugar amount remain 2

# so its not mutable?
   
# but actually it is reffering to 12 inspite of changing the value of 2 
# the value 2 still remain there 

# but how you prove it?

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# Now you can see that  id of 2 is 140711164707784 and 
#  id of 12 is  140711164707784 that is different
#  thats shows value are not changed it just i.eidentity is reffering to another value
