import random

print('Welcome to the online game of Rock Paper Scissors!')
print( )
print('Rules:')
print( )
print('- Player and computer both choose one of the three: rock, paper, or scissors.')
print('- Paper beats rock, rock beats scissors, scissors beat paper')
print( )
print('Lets begin!')

print( )

game1 = input('Choose Rock, Paper, or Scissors: ')
print()
print()
print()




computer = random.choice(['rock', 'paper', 'scissors'])

print('Your guess was ' + str(game1))
print('The computers guess was ' + str(computer))

print( )

if game1 == 'rock' and computer == 'paper' :
	print('You lost! Paper covers rock.')
if game1 == 'paper' and computer == 'rock' :
	print('You win! Paper covers rock.')
if game1 == 'scissors' and computer == 'paper' :
	print('You win! Scissors cut paper.')
if game1 == 'paper' and computer == 'scissors' :
	print('You lost! Paper covers scissors.')
if game1== 'rock' and computer == 'scissors' :
	print('You win! Rock crushes scissors.')
if game1 == 'scissors' and computer == 'rock' :
	print('You lose! Rock crushes scissors.')
if game1== 'rock' and computer=='rock':
	print('Its a tie!')
if game1== 'paper' and computer == 'paper':
	print('Its a tie!')
if game1== 'scissors' and computer == 'scissors':
	print('Its a tie!')



