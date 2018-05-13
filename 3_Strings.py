# Strings in python are immutable
# Once a string is defined it cannot be changed

# A python program to show that string cannot be changed in python

a = 'Nerd Nerd Nerd'
print a		# Display the string

#a[2] = 'E'
print a		# Attempt to change the second character of the string causes error

# A python program to show that a string can be appended to a string

a = a + ', you are !'
print a		# displays the appended output


# A string in python can be created in 3 ways : 
a = 'Learning'			# string with single quotes
b = "Python"			# string with double quotes
c = '''Today I am 
learning Python and I think 	
I am doing pretty fine '''	# string with triple quotes

print a
print b
print c


# A string with triple quotes is used when we have to write a string in multiple lines and printing as it is without using any escape sequence.

# Concatenation of strings
print a+b+c


# print single, double quote in string. This can be done in 2 ways
# 1. First one is to use escape character to display additional quote.
# 2. Second one is to use mix quote.

# use of escape sequence
print "Hi Mr. Bobo"
print "He said , \"which roll do you want , sir?\""
print "Kuch bhi dedo bhaiya!"
print 'And then he said, " thik hai bhaishahab! "'

# A python program to illustrate slicing in strings
x = "Bobo at work"

# Prints 3rd character beginning from 0
print x[2]

# Prints 7th character
print x[6]

# Prints the 3rd character from the rear, with the rear index beginning at -1
print x[-3]

# Length of string is 10. So this one is out of bounds
#print x[15]


# The concept of slicing in strings
# To extract substring from the whole string then we use the syntax like
# string_name[beginning: end: step]

# Beginning represents the starting index of string
# end denotes the end index of string which is 'not inclusive'

# Prints the substring from 2nd to 5th character
print x[2:5]

# Prints substring stepping up 2nd character from 4th to 10th character
print x[4:10:2]

# Prints 3rd character from rear from 3 to 5
print x[-5:-3]




