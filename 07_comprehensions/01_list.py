menu =[
    "Masala chai",
    "Iced lemon tea",
    "Green tea",
    "Iced peach tea",
    "ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
iced_tea = [tea for tea in menu if len(tea)>12]

print(iced_tea)