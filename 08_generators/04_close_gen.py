

def local_chai():
    yield "Masala chai"
    yield "ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

#  close half way through  the code
#  try and except

def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
    except:
           print("stall closed, no more chai order ")
    

stall = chai_stall()
print(next(stall))
stall.close() # clean up memory
