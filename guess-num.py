import random

r = random.randint(1, 100)
count = 0
while True:
	num = input('請猜1~100中的任一個數字')
	num = int(num)
	count = count + 1
	if r == num:
		print('耶!!你猜對了', '你猜了', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')