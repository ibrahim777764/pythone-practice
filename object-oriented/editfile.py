# #read
# file = open("chease.txt", "r")
# lines = file.readlines()
# file.close()

# #edit

# # lines = ("hey my\n" ,"name ibrahim")
# lines.insert(0 , "welcome to ibnas\n")
# lines.insert(10 , "hey my name is ibnas\n")


# #write

# file = open("numbers.txt", "w")
# file.writelines(lines)
# file.close()

#read
file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

#edit

for x in range(len(lines)):
     try:
        number = float(lines[x])*2 
        lines[x] = f"{number}\n"
     except:
      pass


#write

file = open("numbers.txt", "w")
file.writelines(lines)
file.close()

