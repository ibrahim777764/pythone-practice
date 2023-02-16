
import random
import time

name = input("what is your name: ")
time.sleep(3)

print(f"welcome {name}")


guess = int(input("guess secret number: "))
correct_number = random.randint(1,20)
guess_count = 0

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("go highter: "))

    else:
         guess = int(input("go lower: "))

print(f"congrats {name}! correct number is {correct_number} you took {guess_count} attempts")         

        


