import random

x = input('請輸入起始值')
x = int(x)
y = input('請輸入終值')
y = int(y)
r = random.randint(x, y)
count = 0
while True:
	print('範圍為', x, '到', y)
	num = input('請猜一個數字')
	num = int(num)
	count = count + 1
	if r == num:
		print('耶!!你猜對了', '你猜了', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')