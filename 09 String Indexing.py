## Indexing : accessing element of a sequence using [] [indexing operators: start:end:step]

# Indexing always starts from 0, so the first element index is 0

credit_number = "1234-3456-5678-7890"
print("First element is: ",credit_number[0])
print("Fifth element is: ",credit_number[4])

#[start:end]
# This will also include the "-""
print("Element from 1-10", credit_number[1:10])

# [start:end:step]
# This is skip event 2nd number and print the next, step=2
print(credit_number[0:19:2])

# -1, will take the last element of the credit_number
print(credit_number[-1])
# -2, will take the 2nd last element of the credit_number
print(credit_number[-2])

print(credit_number[0:-1:2])

# to reverse the whole credit number
print("Reverse credit number: ",credit_number[::-1])

# to access last 4 digits
print("Last 4 digit's : ", credit_number[-4:])
print(f"Typical crdeit card number showed : XXXX-XXXX-XXXX-{credit_number[-4:]}")
