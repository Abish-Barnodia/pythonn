def make_chai():
    #  return "here is your masal chai"
    print("here is your masala chai")

return_value = make_chai()

print(return_value)

# Nothing->implicitly return none value
def idle_chaiwala():
    pass

print(idle_chaiwala())

# return one value
def sold_cups():
    return 120

total = sold_cups()
print(total)

#  early from function
def chai_status(cups_left):
    if cups_left==0:
        return "Sorry, chai over"
    return "chai is ready"
    return "chai"# its does not return as we did short circuting 
print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 100,20, 10#sold , remaning

sold, remaning, not_paid = chai_report() # or not_paid = _ it also works
print("sold:", sold)
print("remaning:", remaning)