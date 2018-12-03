#!/usr/bin/python3
from time import sleep


# Opening the imnput file
filename = "input.txt"
file = open(filename, "r")
file_data = file.readlines()

# Setting up intial values
result = 0
results = {}
found = False
duplicate = 0

# Adding the values to the sum
while not found:
  for line in file_data:
     value = int(line)
     result += value

     if result not in results:
       results[result] = result
     elif not found:
       found = True
       print("First duplicate:" + str(result))

# Exiting the file
file.close()



