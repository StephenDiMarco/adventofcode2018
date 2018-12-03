#!/usr/bin/python3

# Opening the imnput file
filename = "input.txt"
file = open(filename, "r")

# Zeroing the sum
sum = 0

# Adding the values to the sum
for line in file:
   sum += int(line)

# Exiting the file
file.close()

# Printing the sum
print(sum)
