#python file with solutions to codewars questions

#function to
def divisors(integer):
	output = []
	if type(integer) == int:
		for num in range(2, integer+1):
			if integer % num == 0:
				output.append(num)
			# else:
			# 	return [integer]
		return output
	else:
		return [integer]
print(divisors(20))


# ROMAN NUMERAL DECODER
# link: https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

# Ensure to come back to this to understand how to access dictionaries and their values using index.

standard = {
	'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000
}


def convertRomanToInt(user_input):

	total = 0
	for i in range(len(user_input)):
		if i+1 < len(user_input) and standard[user_input[i]] < standard[user_input[i+1]]:
			total -= standard[user_input[i]]
		else:
			total += standard[user_input[i]]

	print(total)

