def serve_chai():
    yield "Cup 1: Masala chai"
    yield "cup 2: Ginger chai "
    yield "cup3: Elachi chai"

stall = serve_chai()


for cup in stall:
    print(cup)

# regular function
def get_chai_list():
    return["cup1","cup2","cup3"]

# generator function 

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai = get_chai_gen()
print(next(chai)) # cup 1
print(next(chai)) # cup 2
print(next(chai)) # cup 3