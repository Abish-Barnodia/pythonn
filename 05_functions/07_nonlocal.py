def update_order():
    chai_type ="Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print("after kitchen update", chai_type)

update_order()

# function ka ander agar access chaia toh non local ka use kro
# function ka bhar aCCESS chia toh global kia use kro
