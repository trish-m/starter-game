import random


print('''********** [Rock-Paper-Scissors] **********\n
            ~~ Game rules ~~\nRock beats Scissors\nPaper beats Rock\nScissor beats Paper\n''')

possible_choices = ["R", "P", "S"]

invalid_choice = True
while True:
    
  player_input = input("Enter a choice \nR for Rock, P for Paper, S for Scissors: ")
  if player_input in possible_choices: 
    invalid_choice = False

  else:
    print('Invalid choice')
    continue
  

  if player_input == 'R':
    player_choice = 'Rock' 

  elif player_input == 'P':
    player_choice = 'Paper'
  
  elif player_input == 'S': 
    player_choice = 'Scissors'


  computer_input = random.choice(possible_choices)
  if computer_input == 'R':
    computer_choice = 'Rock'

  elif computer_input == 'P':
    computer_choice = 'Paper'
  
  elif computer_input == 'S': 
    computer_choice = 'Scissors'


  print(f"\nPlayer ({player_choice}) : CPU ({computer_choice})\n")

  
  if player_input == computer_input:
    print("It's a tie!\n")
  
  else:
    print('Winner!!!')
    break