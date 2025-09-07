# Now we can see the example of mutability 
# i.e on changing the value the value will will be changed
spice_mix = set()
print(f"Initial spice mix id:{id(spice_mix)}")
print(f"Initial spice mix id:{spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardamom")


print(f"Initial spice mix id:{spice_mix}")
print(f" After Initial spice mix id:{id(spice_mix)}")



# now we see here both the ids are same so it is mutable 