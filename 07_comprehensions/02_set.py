favourite_chais=[
    "Masala chai","Green Tea","Masala chai",
    "Lemon Tea", "Green Tea","Elachi chai"
]

unique_chai ={ chai for chai in favourite_chais if len(chai) > 8}
print(unique_chai)



recipes = {
    "Masala chai" : ["ginger","cardamom", "clove"],
    "Elachi Chai" : ["cardamom", "milk"],
    "spicy chai"  :["ginger","black pepper" ,"clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)