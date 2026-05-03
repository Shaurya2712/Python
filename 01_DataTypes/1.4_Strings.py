# String is a datatye in python. It is immutable

# Strings
Air_Force = "Air Force"
Indian_Army = "Indian Army"
Indian_Navy = "Indian Navy"

# Printing the Strings
print(
    f"Following are the defence forces of the indian army : "
    f"{Air_Force}, "
    f"{Indian_Army}, "
    f"{Indian_Navy}"
)

# Indexing
my_hobby = "I will start to go for running again in the morning"

print(f"The first letter of the string my_hobby is = "
      f"{my_hobby[0:10:1]}"
      )

print(f"Reverse of the string is : "
      f"{my_hobby[::-1]}"
      )

# To print Special character strings (specially other languages)
label_text = "here is the special character : ǎ r̥"
print(f"label_text : {label_text}")

# encoding the special symbol string
encoded_label_text = label_text.encode("utf-8")
print(f"encoded_label_text: {label_text}")

# decoding the special symbol string
decode_label = encoded_label_text.decode("utf-8")
print(f"decode_label: {label_text}")
