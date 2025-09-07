chai_type = "irani"

def order():
    def typ():
        global chai_type
        chai_type=" elachi"
    typ()

order()
print(chai_type)