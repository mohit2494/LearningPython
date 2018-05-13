# Program for understanding Variables, Expressions, Conditions and Functions 

# Variables need not be declared first in Python. They can be used directly. Variables in python are case sensitive as most of the other programming languages.

a = 3
A = 4  
print a
print A	# a and A are different variables


# Expressions in Python

c = a + A # Simple Addition
d = a * A # Simple Multiplication

print c
print d

# Conditions in Python

if c % a == 0 :
	print "c is divisible by a"
else : 
	print "you are in the else statement. c is not divisible by a."


# Functions in Python

# A function in python is declared by the keyword 'def' before the name of the function. The return type of the function need not be specified explicitly by python. The cuntion can be invoked by writing the function name followed by the parameter list in the brackets.

# Function for checking the divisibility
# Notice the indentation after the function declaration
# and if and else statements

# Start of function 
def checkDivisibility(a,b) :
	if a % b == 0 :
		print "a is divisible by b"
	else : 
		print "a is not divisible by b"
# End of function









