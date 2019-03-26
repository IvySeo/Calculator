#!/usr/bin/python
# 		This is the program that mimics the basic functions of a calculate, adding
#		subtracting, multiplying, dividing, modular, and telling if a number is an even or odd
#		and if the number is prime.
import string

# Pre condition: Ask the user to enter two rational number
# This function adds two numbers
# Post condition: Adds those two numbers and returns the result
def add(x, y):
	return x + y

# Pre condition: Ask the user to enter two rational number
# This function subtracts two numbers
# Post condition:Subtracts those two numbers and returns the result
def subtract(x, y):
   return x - y

# Pre condition : Ask the user to enter two rational number
# This function multiplies two numbers
# Post condition : it takes the product of those two numbers and returns the result
def multiply(x, y):
   return x * y

# Pre condition: Ask the user to enter two rational number
# This function divides two numbers
# Post condition :it divides those two numbers and returns the result
def divide(x, y):
   return x / y

# Pre condition : Ask the user to put the one valid number
# This function checks if that number s even or odd and return the result.
# Post condition: The function "EvenCheck" check if that number is even or odd and return the result.
def EvenCheck(x):
	if(int(x) % 2 == 0):
		return True
	else:
		return False

# Pre condition : Ask the user to insert one valid number
# This function returns if the given number is prime number or not
# Post condition: The function "PrimeCheck" returns if the given number is prime number or not.
def PrimeCheck(x):
	for i in range(2, int(x/2)):
		if(x % i == 0):
			return False
	return True

# pre condition: Ask the user to input two rational numbers
# This function modules two numbers
# post condition: The modular function return the remainder of those two numbers
def modular(x, y):
   return int(x) % int(y)

def help():
	print("1. Addition : Add up two rational numbers" )
	print("2. Subtraction : Subtract two rational numbers" )
	print("3. Multiplication : multiply two rational numbers" )
	print("4. Division : Divide two rational numbers" )
	print("5. Even/Odd : Tells whether the number is even or odd" )
	print("6. Prime : Tells whether the number is prime or not" )
	print("7. Modular function returns the remainder")

#Guide the user by telling what each function does
#displays main menu for user to follow
def Menu():
	print("\n"*2+"-"*70)
	print("{0: ^70}".format("Welcome to the mini calculator"))
	print("{0: ^70}".format("*"*15))
	print("{0: ^70}".format("Enter 'H' for help 'Q' for quit. Enjoy :)"))
	print("-"*70+"\n"*3)
	print("{0:.<50}".format("Enter the function Character you want to operate."))
	print("{0:.<50}".format("*Addition --- type 'A'"))
	print("{0:.<50}".format("*Subtraction --- type 'B'"))
	print("{0:.<50}".format("*Multiplication  --- type 'C'"))
	print("{0:.<50}".format("*Division  --- type 'D'"))
	print("{0:.<50}".format("*Even/Odd --- type 'E'"))
	print("{0:.<50}".format("*Prime --- type 'F'"))
	print("{0:.<50}".format("*Modular function --- type 'G'"))
	print("{0:.<50}".format("*Help --- type 'H'"))
	print("{0:.<50}".format("*Quit the program --- type 'Q'"))

# the main "meat" of the program
# There is a loop where the program will run until the user tells it to stop
# the loop will take in a user input and will do the requested operations
# on he number that the user also enters
def basic_calculator():
	again = "Y"
	while(again == "Y"):
		#call the menu function to display menu
		Menu()

		#ask user and get the choice
		option = raw_input("What is your choice? : ")

		option = option.upper()

		#Add
		if option == "A":
			num1 = 0
			num2 = 0
			while True:
				try:
					num1 = float(raw_input("Enter first number: "))
					num2 = float(raw_input("Enter second number: "))
				except ValueError:
					print("Please enter a valid number!")
					continue
				else:
					break
			print(num1,"+",num2,"=", add(num1,num2))

		#Subtract
		elif option == "B":
			num1 = 0
			num2 = 0
			while True:
				try:
					num1 = float(raw_input("Enter first number: "))
					num2 = float(raw_input("Enter second number: "))
				except ValueError:
					print("Please enter a valid number!")
					continue
				else:
					break
			print(num1,"-",num2,"=", subtract(num1,num2))

		#Multiply
		elif option == "C":
			num1 = 0
			num2 = 0
			while True:
				try:
					num1 = float(raw_input("Enter first number: "))
					num2 = float(raw_input("Enter second number: "))
				except ValueError:
					print("Please enter a valid number!")
					continue
				else:
					break
			print(num1,"*",num2,"=", multiply(num1,num2))

		#Divide
		elif option == "D":
			num1 = 0
			num2 = 0
			while True:
				try:
					num1 = float(raw_input("Enter first number: "))
					num2 = float(raw_input("Enter second number: "))

					if num2 == 0:
						print("The second number cannot be zero, Please try again")
					continue

				except ValueError:
					print("Please enter a valid number!")
					continue
				except ZeroDivisionError:
  					continue
				else:
					break
			print(num1,"/",num2,"=", divide(num1,num2))

		#even or odd
		elif option == "E":
			num1 = 0
			while True:
				try:
					num1 = int(raw_input("Enter one number: "))
				except ValueError:
					print("Please enter a valid number!")
					continue
				else:
					break

			if(EvenCheck(num1) == True):
				print(num1, " is Even." )
			else:
				print(num1, " is Odd." )

		#Prime
		elif option == "F":
			num1 = 0
			while True:
				try:
					num1 = int(raw_input("Enter one number: "))
				except ValueError:
					print("Please enter a valid number!")
					continue
				else:
					break

			if(PrimeCheck(num1) == True):
				print(num1, " is Prime." )
			else:
				print(num1, " is Not Prime." )

		#Modular
		elif option == "G":
			num1 = 0
			num2 = 0
			while True:
				try:
					num1 = float(raw_input("Enter first number: "))
					num2 = float(raw_input("Enter second number: "))
				except ValueError:
					print("Please enter a valid number!")
					continue
				else:
					break
			print(num1,"%",num2,"=", modular(num1,num2))

		#help menu
		elif option == "H":
			help()

		#quit
		elif option == "Q":

			# program quit
			exit()

		#error detect
		else:
		   print("Invalid input")

		print("Would you like to continue? (Y (yes) or N (no))")
		again = raw_input("==> ")
		again = again.upper()

basic_calculator()

print("Calculator is ending. Good bye.")