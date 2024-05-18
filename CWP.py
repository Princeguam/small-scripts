def divisors(integer):
	output = []
	if type(integer) == int:
		for num in range(2, integer):
			if integer % num == 0:
				output.append(num)
			# else:
			# 	return [integer]
		return output
	else:
		return [integer]
print(divisors(11))
