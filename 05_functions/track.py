import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+917652968046")
print("Phone number location:")
print(geocoder.description_for_number(phone_number1, "en"))
