import sys


file = open ("chease.txt", "x")

file.write("hey")

file.close()

file = open ("argument.txt", "w")

file.write("1,2,3")

file.close()


import sys

file_name = sys.argv[1]

file = open(file_name, "w")

file.close()

