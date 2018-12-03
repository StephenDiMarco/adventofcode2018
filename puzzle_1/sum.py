#!/usr/bin/python3

filename = "input.txt"
file = open(filename, "r")
sum = 0
for line in file:
   sum += int(line)

print(sum)
