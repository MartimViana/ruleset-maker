import os
###
# Keywords
'''
	Keywords are words that have a special meaning to the compiler.
	No keywords must be present on the class creation dictionary
'''
keywords = {
	'class name' : 'className',
	'class type' : 'classType',
	'no arguments allowed' : 'no-arg '
}

keywords_class_type = {
	
}

def newBlock(variables):
	keys = variables.keys()	# Get list of keys

	# Write to file
	file = open(variables[keywords['class name']]+".py", 'wb')

	# Declare nuclear composnents of all classes
	declareClass(file, variables[keywords['class name']])
	declareInitializer(file, variables)

	# Declare specific parts of all classes
	declareSpecificClassType(file, variables)

'''

'''
def declareClass(file, name):
	write(file, "class " + name + ":\n")

'''

'''
def declareInitializer(file, variables):
	# get initializer arguments
	temp = getAllValuesExceptKeywords(variables)
	tempWithCommas = ''
	for t in temp:
		if notKeywords(t):
			tempWithCommas += ', ' + t

	# Write arguments on initializer
	write(file, "\tdef __init__(self" + tempWithCommas + "):\n")

	# declare constructor structure
	for key in variables.keys():
		if notKeywords(key):
			write(file, "\t\t" + key + " = " + str(variables[key]) + "\n")

	file.close()

def declareSpecificClassType(file, variables):
	print("todo")

'''

'''
def getAllValuesExceptKeywords(variables):
	result = []
	for value in variables:
		result.append(value)
	return result


'''

'''
def notKeywords(string):
	return not string in keywords.values() 

'''

'''
def write(file, string):
	file.write(string.encode('utf-8'))