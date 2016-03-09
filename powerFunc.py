def float_input(prompt):
	"""Accepts a promt for the user as a string, returns their answer as a float
	Allows user to try again. """
	userNumber = input(prompt)
	finalNumber = None
	while finalNumber != userNumber:
		try:
		#checks if its a number
			userNumber = float(userNumber)
		#only put lines that you expect to cause exceptions here
		except ValueError:
			userNumber = input("That is'nt a number, try again:")
		else:
			finalNumber = userNumber
	
	return userNumber

def power(number, expNum):
	#"""Converts a 2 inputs into a base and an exponent without use in **"""
	ogNum = number
	while expNum != 1:
	
		number *= ogNum
		expNum -= 1
	return number

	
expNum = float_input("Choose a value for your exponent. ")
value = float_input("Choose a number for your base. ")
answer = power(value, expNum)
print ("{} to the power of {} is {}".format(value, expNum, answer))
