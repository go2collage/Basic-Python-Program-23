# Basic Python Program

# multiplies all the items in a list
# Subtracts all the items in a list

list2 = [10, 20, 30, 40, 50]
i = 0
mul = 1
sub = 0

for x in list2:
    mul = list2[i] * mul    # Multiplication
    sub = list2[i] - sub    # Subtraction
    i = i + 1

print("Multiplies all the items in a list is: ", mul)
print("Subtraction all the items in a list is: ", sub)


