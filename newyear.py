from random import randint
import time


for i in range(1, 60):
	print('')

s = ''

for i in range(1, 1000):
	count = randint(1, 500)
	while count > 0:

		s += ' '
		count -= 1
	
	if i % 10 == 0:

		print(s + 'Happy New Year')

	elif i % 91 == 0:

		print(s + 'Merry Chritmas')

	else:
		rand = randint(0, 2)
		if rand >= 1:

			print(s + "*")

		else:

			print(s + "X")


	s = ''
	time.sleep(0.15)