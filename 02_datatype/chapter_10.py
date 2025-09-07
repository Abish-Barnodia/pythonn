# dictonary : instead of 0 and 1 names are stored 
# in the form of first_name and last_name
# in dictonary order doesn't matter

chai_order = dict(type = "Masala Chai", size="Large",sugar=2)
print(f"chai order : {chai_order}")

chai_recipe = {}
# add data
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base: {chai_recipe['base']}")

# before removing data
print(f"recipe : {chai_recipe}")

# After remove data
del chai_recipe["liquid"]
print(f"recipe : {chai_recipe}")

# whenever there is data there is membership test

print(f"Is sugar in the order? {'sugar' in  chai_order}")

# key->type,size,sugar
# values-> ginger chai ,medium,1
chai_order = {"type" :"Ginger Chai","size":"Medium","sugar" :1}
print(f"Order details(keys): {chai_order.keys()}")
print(f"Order details(values): {chai_order.values()}")

# get all the items 
print(f"Order details(items): {chai_order.items()}")

# pop the last item
last_item = chai_order.popitem()
print(f"removed last item : {last_item}")

# update the item

extra_spices ={"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"updated chai recipe : {chai_recipe}")

chai_order = {"type" :"Ginger Chai","size":"Medium","sugar" :1}

customer_note= chai_order.get("note","No Note")
print(f"customer_note is : {customer_note}")

customer_note= chai_order.get("size","No Note")
print(f"customer_note is : {customer_note}")
