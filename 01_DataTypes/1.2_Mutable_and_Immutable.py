# CONCEPT OF MUTABLE and IMMUTABLE

# IMMUTABLE:
# It is NOT Changeable
# When Checking for the immutability, always compare with the Id
# a.k.a. Identity instead of the Value.

# MUTABLE:
# It is Changeable
# When Checking for the mutability, always compare with the Id
# a.k.a. Identity instead of the Value.

# ----------IMMUTABLE----------

# This is an example of immutable objects (strings).
# Here, we are not modifying the original string.
# Instead, the variable 'car_name' is reassigned to a new string object.
# Strings are immutable, so their value cannot be changed.

# Runnable Code---
car_name = "mustang"
print(f"This is the mustang car_name value:{id("mustang")}")
print(f"This is the car_name id:{id(car_name)}")

car_name = "ferrari"
print(f"This is the ferrari car_name value:{id("ferrari")}")
print(f"This is the car_name id:{id(car_name)}")

# Output---
# This is the mustang car_name value:   4313131376
# This is the car_name id:              4313131376
# This is the ferrari car_name value:   4313131808
# This is the car_name id:              4313131808


# ----------MUTABLE----------

# Here we use set a datatype used for the collection of set
# Set is like a collection of somthing in which we can append or subtract
# I am going to save multiple squadrons in it stating how a set is mutable and
# can store multiple values in it and the ID remains same for it.

# Declared a new set here
Sqaudrons_in_airforce_academy = set()
print(f"Initial Id of the set: {id(Sqaudrons_in_airforce_academy)}")

Sqaudrons_in_airforce_academy.add("AQUINO")
print(f"Id of the set after AQUINO: {id(Sqaudrons_in_airforce_academy)}")

Sqaudrons_in_airforce_academy.add("KATRE")
print(f"Id of the set after KATRE: {id(Sqaudrons_in_airforce_academy)}")

Sqaudrons_in_airforce_academy.add("CHITNIS")
print(f"Id of the set after CHITNIS: {id(Sqaudrons_in_airforce_academy)}")

Sqaudrons_in_airforce_academy.add("BRAR")
print(f"Id of the set after BRAR: {id(Sqaudrons_in_airforce_academy)}")

Sqaudrons_in_airforce_academy.add("DESA")
print(f"Id of the set after DESA: {id(Sqaudrons_in_airforce_academy)}")

Sqaudrons_in_airforce_academy.add("NAIDU")
print(f"Id of the set after NAIDU: {id(Sqaudrons_in_airforce_academy)}")

print_message = (
    f"Sqaudrons_in_airforce_academy contents: "
    f"{Sqaudrons_in_airforce_academy}"
)

print(print_message)

# Output---
# Initial Id of the set:        4456154720
# Id of the set after AQUINO:   4456154720
# Id of the set after KATRE:    4456154720
# Id of the set after CHITNIS:  4456154720
# Id of the set after BRAR:     4456154720
# Id of the set after DESA:     4456154720
# Id of the set after NAIDU:    4456154720
# Sqaudrons_in_airforce_academy contents: {'CHITNIS', 'DESA', 'KATRE',
# 'NAIDU', 'BRAR', 'AQUINO'}
