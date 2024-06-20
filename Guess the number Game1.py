import random
import math


lower_bound = int(input("Enter Lower Bound : "))
upper_bound = int(input("Enter Upper Bound : "))

number = random.randint(lower_bound , upper_bound)
Chances = round(math.log(upper_bound - lower_bound + 1 , 2))
print(f"Total Chances : {Chances}")

count = 0
while count < Chances:
    count = count + 1
    guess = int(input("Enter Your Guess : "))
    if guess == number:
      print(f"Congratulations! You have guessed in {count} chances")
      break 
    elif guess > number:
      print("Try Again! You guessed too high")
    elif guess < number:
      print("Try Again! You guess too small")
    
if count >= Chances:
  print(f"The Number Is : {number}\nBetter Luck Next Time")