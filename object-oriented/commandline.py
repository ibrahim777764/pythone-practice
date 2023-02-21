import sys

total = 1
for argument in sys.argv:
     try:
        number = float(argument)
        total *= number
     except:
      pass

print(total)
