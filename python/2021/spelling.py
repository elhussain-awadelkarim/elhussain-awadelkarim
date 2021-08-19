# Spelling Game

# Imports 
import time
import math
import random
# Words
# Dice
def dice_simulate():
    number = random.randint(1,6)
    print(number)

# Intro
mode = input("(1) player or (2) player mode: ")
if mode == "1":
	name = input("Enter name: ")
	age = input("Enter age: ")
	print("Hello " + name + "!")
	time.sleep(1)
	print("Correct the spelling mistakes in the sentences.")
	time.sleep(1)
	print("			01")
	time.sleep(1)
	print("			02")
	time.sleep(1)
	print("			03")
	time.sleep(1)
	print("			GO!")
	time.sleep(1)
	if age == "9":
		sen_1 = "The rabit hoped ovar the fnce."
		cor_1 = "The rabbit hopped over the fence."
		sen_2 = "You nead good solil to growe fruit trees."
		cor_2 = "You need good soil to grow fruit trees."
		sen_3 =	"I will go to shcool starting next weak."
		cor_3 = "I will go to school starting next week."
		sen_4 = "Our bus wont strat becuase the battry is flat."
		cor_4 = "Our bus won't start because the battery is flat."
		score = 0
		
		print("Correct this sentence\n" + sen_1)
		int_1 = input("> ")
		if int_1 == cor_1:
			score += 1
		print("Correct this sentence\n" + sen_2)
		int_2 = input("> ")
		if int_2 == cor_2:
			score += 1	 
		print("Correct this sentence\n" + sen_3)
		int_3 = input("> ")
		if int_3 == cor_3:
			score += 1
		print("Correct this sentence\n" + sen_4)
		int_4 = input("> ")
		if int_4 == cor_4:
			score += 1
		print(str(score) + "/4")
		time.sleep(2)
		quit()
elif mode == "2":
	name_1 = input("Enter name player 1: ")
	age_1 = input("Enter grade: ")
	name_2 = input("Enter name player 2: ")
	age_2 = input("Enter grade: ")
	print("Hello " + name_1 + "!")
	time.sleep(1)
	print("Hello " + name_2 + "!")
	time.sleep(1)
	
#else:
#	print("Thats not a option!")
#	quit()
