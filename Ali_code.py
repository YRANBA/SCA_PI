import random
answer = random.randint(1,10)
guess = int(raw_input('guess a number from 1-10'))
while answer!= guess:
	guess = int(raw_input('guess a number from 1-10'))
	if guess < n:
		print 'guess is too low'
	else:
		if guess > n:
			print 'guess is too high'
		else:
			print 'you guessed it'
			#break
