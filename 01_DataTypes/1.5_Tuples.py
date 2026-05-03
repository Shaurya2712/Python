# Tuples, immutable (cannot be change)
Car_components = {"engine", "Headlight", "rearlight"}
(part1, part2, part3) = Car_components

# Printing the statements
print(f"part1 is {part1}")
print(f"part2 is {part2}")
print(f"part3 is {part3}")

# Direct assignment
Car_wheels, Car_seats = 4, 6
print(f"Car_wheels is {Car_wheels}")
print(f"Car_seats is {Car_seats}")

# Reverse assignment
Car_wheels, Car_seats = Car_seats, Car_wheels
print(f"Car_wheels is {Car_wheels}")
print(f"Car_seats is {Car_seats}")

# Membership (To confirm if a variable is part of the tupples)- 
# it is case sensitive
print(f"is engine part of Car_components ? \{'engine' in Car_components}") #True
print(f"is engine part of Car_components ? {'Engine' in Car_components}") #False
