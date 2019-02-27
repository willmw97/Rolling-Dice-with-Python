from random import *
	def options():
	again = input('Roll again y or n?')
		return again == 'y' # returns True if player rolls again
	def diceRoll(n):
	total_points = 0
	for i in range(0, n):
		turn_points = 0
	while True:
		points = []
		rollList = []
	for i in range(5):
		rollList.append(randint(1, 6))
			print(rollList)
		specialdie = rollList[0]
			print("Special Dice has been rolled", specialdie)
		if specialdie == 3:
		if rollList.count(1) == 2:
			points.append(100)
		elif rollList.count(2) == 2:
			points.append(20)
		elif rollList.count(3) == 2:
			points.append(30)
		elif rollList.count(4) == 2:
			points.append(40)
		elif rollList.count(5) == 2:
			points.append(50)
		elif rollList.count(6) == 2:
			points.append(60)
		else:
			points.append(5)
		if specialdie != 3:
		if rollList.count(1) == 5:
			print("You lost")
			return
		if rollList.count(6) == 5:
			print("You won")
			return
		elif rollList.count(1) == 3:
			points.append(100)
		elif rollList.count(2) == 3:
			points.append(20)
		elif rollList.count(3) == 3:
			points.append(30)
		elif rollList.count(4) == 3:
			points.append(40)
		elif rollList.count(5) == 3:
			points.append(50)
		elif rollList.count(6) == 3:
			points.append(60)
	else:
		for num in rollList:
			if num == 5:
				points.append(5)
			if num == 1:
				points.append(10)
# player loeses round gets message:
# print message
# turn_points = 0
		a = sum(points)
		print('Points in turn' + str(a))
		if not roll_again:
		break
		turn_points += total_points
diceRoll(1000)

