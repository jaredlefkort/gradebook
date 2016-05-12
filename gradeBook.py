#Jared Lefkort
#Date: 5/12/16

grades = [[100, 95, 97, 86, 70],
		  [98, 100, 92, 88, 83],
		  [92, 95, 89, 100, 86]]

def average_grade(grades):
	averages = []
	
	counter = 0
	numbers = 0
	for row in grades:
		numbers = 0
		counter = 0
		for item in row:
			numbers += item
			counter += 1
		average = numbers / counter

		averages.append(average)
	return averages

def class_average(list):
	classTotal = 0
	classCounter = 0
	for row in list:
		for item in row:
			classCounter += 1
			classTotal += item
			classAverage = classTotal / classCounter
	return classAverage

print(average_grade(grades))
print("The class average is {}".format(class_average(grades)))	