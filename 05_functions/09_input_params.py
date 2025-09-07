chai = " ginger chai"

def prepare_chai(order):
    print("preparing",order)

prepare_chai(chai)
print(chai)


chai = [1,2,3]
def edit_chai(cup): #parameter :cup
    cup[1] = 42

edit_chai(chai) # args = chai
print(chai)


# args : positional parametes -> arguments
#  *kwargs : another parameters ->key value arguments


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("darjeeling","yes","low")#optional
make_chai(tea="green", milk="no", sugar="medium" )# keywords


def special_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

special_chai("Cinnamon", "Cardmon", sweetener ="honey ", foam="yes") 

def chai_order(order=[]):
    order.append("Masala")
    print(order)

def chai_order(order=None):
    if order is None:
        order =[]
        print(order)

chai_order()
chai_order()