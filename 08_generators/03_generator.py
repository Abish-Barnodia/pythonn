

# yield send data

def chai_customer():
    print("welcome ! what chai would you like ?")
    order = yield 
    while True:
        print(f"prerparing: { order}")
        order = yield

stall = chai_customer()
next(stall) # start thr generator

stall.send("masala chai")
stall.send("lemon chai")
stall.send(" elachi chai")