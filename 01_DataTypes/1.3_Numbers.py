# Number are categorized in following:
# Integers
# Boolean and Logical operations
# Real (floating - decimal)
# Complex (number with the imaginary part)

# Integers---
number_one = 8
number_two = 23
number_three = 10_00_00_000

# 1 Addition (+)
addition_part = number_one + number_two
print(f"total_part_one = {addition_part}")

# 2 Subtraction (-)
subtraction_part_positive = number_two - number_one
print(f"subtraction_part_positive = {subtraction_part_positive}")

subtraction_part_negative = number_one - number_two
print(f"subtraction_part_negative = {subtraction_part_negative}")

# 3 Multiplication (*)
multiplication_part = number_one * number_two
print(f"multiplication_part = {multiplication_part}")

# 4 Division (/)
division_part_1 = number_one / number_two
print(f"division_part_1 = {division_part_1}")

division_part_2 = number_two / number_one
print(f"division_part_2 = {division_part_2}")

# 5 division with no fraction part needed (//)
division_with_no_fraction_part_1 = number_one // number_two
print(f"division_with_no_fraction_part_1 = {division_with_no_fraction_part_1}")

division_with_no_fraction_part_2 = number_two // number_one
print(f"division_with_no_fraction_part_2 = {division_with_no_fraction_part_2}")

# 6 Modulus (%)
modulas_part_1 = number_one % number_two
print(f"modulas_part_1 = {modulas_part_1}")

modulas_part_2 = number_two % number_one
print(f"modulas_part_2 = {modulas_part_2}")

# 7 Exponential power (**)
exponential_power_part = number_one ** number_two
print(f"exponential_power_part = {exponential_power_part}")

# Output
# total_part_one = 31
# subtraction_part_positive = 15
# subtraction_part_negative = -15
# multiplication_part = 184
# division_part_1 = 0.34782608695652173
# division_part_2 = 2.875
# division_with_no_fraction_part_1 = 0
# division_with_no_fraction_part_2 = 2
# modulas_part_1 = 8
# modulas_part_2 = 7
# exponential_power_part = 590295810358705651712

# Boolean---
# It is either "True" or "False"

is_airforce_interview_preparation_tough = False
is_airforce_screening_tough = True
is_airforce_interview_immpossible_to_crack = False
is_airforce_interview_crackable = True

total_number_of_boolean_questions_answered_positive = (
    is_airforce_interview_preparation_tough
    + is_airforce_screening_tough
    + is_airforce_interview_immpossible_to_crack
    + is_airforce_interview_crackable
)

print(f"total_number_of_boolean_questions_answered_positive: \
{total_number_of_boolean_questions_answered_positive}")

# Output---
# total_number_of_boolean_questions_answered_positive: 2

# So here in the output we can see that the boolean also
# represented as 1(true) and 0(false) so automatically pythin supports
# UPCASTING also


# Logical operations---
# and, or, not
are_you_preparing_for_ssb = True
are_you_able_to_clear_ssb = True
will_you_get_selected = are_you_preparing_for_ssb and are_you_able_to_clear_ssb
print(f"will_you_get_selected = {will_you_get_selected}")
# will_you_get_selected = True

# Real---
ideal_temp = 95.50
current_temp = 95.49
temp_diff = ideal_temp - current_temp
print(f"temp_diff = {temp_diff}")
# temp_diff = 0.010000000000005116
