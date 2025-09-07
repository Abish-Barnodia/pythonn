# types of function
#  pure vs impure
#  recursive function
# Lambdas(Anonymous function)


# pure vs impure

# pure

def pure_chai(cups):
    return cups*10

total_chai =0

# impure
def impure_chai(cups):
    global total_chai
    total_chai+= cups 


# recursive
def pour_chai(n):
    print(n)
    if n==0:
        return " All cups poured"
    return pour_chai(n-1)
print(pour_chai(3))

# lambda 

chai_types =["light", "kadak","ginger","kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))

print(strong_chai)


