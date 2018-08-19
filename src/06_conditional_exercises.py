"""
print(" GUESS A NUMBER GAME ".center(230, "*"))
winning_number = 27
your_guess = int(input("Guess a number between 1 - 100: "))
if winning_number == your_guess:
	print("YOU WIN!!!")
else:
	if your_guess < winning_number:
		print("Too low...")
	else:
		print("Too high...")
"""

"""
print("COCO")
name, age = input("Enter name follow it up age space separated: ").split()

if (name[0] == 'a' or name[0] == 'A') and int(age) >= 10:
	print("Enjoy the movie...")
else:
	print("Sorry! No luck this time...")
"""

"""
print("Check Movie price")

age = int(input("Enter your age: "))

if 1 <= age <= 3:
	print("Watch Free!!!")
elif 4 <= age <= 10:
	print("You pay 100")
elif 11 <= age <= 60:
	print("You pay 200")
else:
	print("You pay 300")
"""

max = 10
for i in range(10):
	if i == 5:
		break
	if i % 2 == 0:
		continue
	print(i)

number, sum = "9876", 0
for i in number:
	sum += int(i)

print(sum)
import random

tries = 0
winning_number = random.randint(1, 100)
while True:
	your_guess = int(input("Guess a number between 1 - 100: "))
	tries += 1
	if winning_number == your_guess:
		print("You win!!! after %d tries" % tries)
		break
	elif your_guess < winning_number:
		print("Too Low...")
	else:
		print("Too High")
