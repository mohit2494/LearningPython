# String functions in python

# 1. Find('string',beg,end) : This function is used to find the position of the substring within a string. It takes 3 arguments, substring, starting index (by default 0) and ending index( by default string length ) 

# It returns -1 if string is not found in the given range

# It returns first occurence of string if found.

str = 'today is a beautiful rainy day'
strFind = 'beautiful'

print('The first occurence of str2 is at: ', end="")
print(str.find(strFind,4))

# Function 2: rfind()
# The function has similar functioning as find(), but it returns the position of last occurence of string.

print('The last occurence of strFind is at: ', end="")
print(str.rfind(strFind,4))

# 3. startswith('string',beg,end) :- The purpose of this function is to return true if the functions begins with mentioned string(prefix)


#4. endswith('string',beg,end) :- The purpose of this function is to return true if the function ends with mentioned string(suffix) else return false.

# Example
# Use startswith() and endswith()

newString = 'it is a beautiful summer morning'		# New Sample String
newStringCheck = 'it'					# Sample string for checking


if newString.startswith(newStringCheck): 
	print('newString begins with newStringCheck')
else : 
	print('newString does not begin with newStringCheck') 

if newString.endswith(newStringCheck):
	print('newString ends with newStringCheck')
else : 
	print('newString does not end with newStringCheck')


# 5. islower('string') : This function returns true if all the letters in the string are lower cased.



#6. isupper('string') : This function returns true if all the letters in the string are upper cased.

stringTestLower = 'this is a lower cased string'
stringTestUpper = 'THIS IS AN UPPER CASED STRING'

print('stringTestLower is lower cased: ', stringTestLower.islower())
print('stingTestUpper is upper cased: ', stringTestUpper.isupper())


#7. lower() : This function returns the new string with all the letters converted into its lower case.
print('stringTestUpper is now converted to all lower case', stringTestUpper.lower())


#8. upper() : This function returns the new string with all the letters converted into its upper case.
print('stringTestLower is now converted to all uppper case', stringTestLower.upper())

#9. swapcase(): This function returns the new string with all the letters swapped with their case.
print('swapping the case of stringTestLower',stringTestLower.swapcase())

#10. converting string into its title case
print('writing stringTestUpper in it\'s title case',stringTestUpper.title())















