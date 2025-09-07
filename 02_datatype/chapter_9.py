# Set

essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

# Union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# intersection
common_spices = essential_spices & optional_spices
print(f"commom spices: {common_spices}")


only_in_essential= essential_spices - optional_spices
print(f"Only in essential spices :{only_in_essential}")

# membership test

print(f"Is 'cloves' in essential spices? {'cloves' in optional_spices}")

# To freeze the set 

# use (frozenset)