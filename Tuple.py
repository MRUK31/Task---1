# Original tuple
tuple = (1, 2, 3)

# Adding a new element
new_element = 4
updated_tuple = tuple + (new_element,)

# Removing an element
updated_tuple = tuple[:1] + tuple[2:]

# Modifying an element
modified_element = 5
updated_tuple = tuple[:2] + (modified_element,) + tuple [3:]

#Printing the Tuple
print(updated_tuple)
