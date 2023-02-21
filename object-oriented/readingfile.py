#first way to read file
file = open("numbers.txt" , "r")

# file_text = file.read()
# print(file_text)

#2nd way to read file
# lines = file.readlines()
# print(lines)

#3rd way to read file
import sys 
total = 1
for argument in file:
     try:
        number = float(argument)
        total *= number
     except:
      pass

print(total)

file.close()

