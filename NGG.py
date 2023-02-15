import random
import time

print("welcome to guessing game! you have to guess number between 1 to 20  ;)")
time.sleep(3)
print("wait, let me pic a number")
time.sleep(2)

guess = int(input("what's your guess: "))
correct_number = random.randint(1,20)
guess_count = 1

while guess != correct_number:
 guess_count += 1
 if guess < correct_number:
  guess = int(input("wrong! guess higher number then this: "))

 else:
     guess = int(input("wrong! guess lower number then this: "))


print(f"congrats ! correct answer is {correct_number} , it took you {guess_count} attempts")