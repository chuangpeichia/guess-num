import random

r = random.randint(1, 100)
while True:
	num = input('請猜1~100中的任一個數字')
	num = int(num)
	if r == num:
		print('耶!!你猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')