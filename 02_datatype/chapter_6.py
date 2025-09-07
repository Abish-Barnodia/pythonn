chai_type = "Ginger chai"
customer_name = "Priya"
print(f"order for {customer_name}:{chai_type} please!")
chai_description ="Aromatic and bold"
# [0:8:2] : index starts at (zero) i.e : A and end at 8 i.e c also having space 2 i.e A_o_a_i
print(f"First word: {chai_description[0:8:2]}")
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")

# -1 is used to reverse the string 
print(f"Last word: {chai_description[::-1]}")

# use  of special symbols like other languages
#encoding and decoding
label_text = "chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decode label: {decoded_label}")