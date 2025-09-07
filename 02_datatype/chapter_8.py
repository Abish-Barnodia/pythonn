# list->Array (Mutable)

ingredients = ["water","milk","black tea"]

# append->add
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

# remove->subtract
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options=["ginger","cardamom"]
chai_ingredients=["water","milk"]

# extend-> add the other variable
chai_ingredients.extend(spice_options)
print(f"chaai: {chai_ingredients}")

# insert-> used to add the position
chai_ingredients.insert(2,"black tea")
print(f"chai: {chai_ingredients}")

# pop()-> uised to remove the elements
last_added= chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

# reverse()-> it will reverse the list not every word of elements
chai_ingredients.reverse()
print(f"chai:{chai_ingredients}")

# sort
chai_ingredients.sort()
print(f"chai:{chai_ingredients}")


sugar_levels=[1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# operator oveerloading
base_liquid = ["water","milk"]
extra_flavour=["ginger"]

full_liquid_mix = base_liquid+ extra_flavour
print(f"liquid mix:{full_liquid_mix}")


strong_brew =["black tea","water"] *3
print(f"string brew{strong_brew}")

# byte array
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data= raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Bytes: {raw_spice_data}")