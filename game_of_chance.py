import random

money = 100

#Write your game of chance functions here
def play_coin_flip(guess, bet):
  toss =  random.randint(1, 2)
  print("Toss is:"+ str(toss))

  #(toss == 1):
    #print("The toss result was head")
  #if(toss == 2):
   # print("The toss result was tail")
  if(guess.lower() == "head" and toss == 1):
    print("You guessed head and your guess is right! You won " + str(bet) + "$!!")
    return +bet
  if(guess.lower() == "tail" and toss == 2):
    print("You guessed tail and your guess is right! You won " + str(bet) + "$!!")
    return +bet
  else:
    print("Your guess was wrong ,Better luck next time! You lost "+str(bet) + "$!!")
    return -bet


#Now you entered in another game named cho han where 2 dices are rolled and you have to guess whether the total is even or odd
def play_cho_han(guess, bet):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  result = dice1 + dice2
  if(result %2 == 0 and guess.lower() == 'even'):
    print("You guessed even and your guess is right! You won " + str(bet) + "$!!")
    return +bet
  if (result % 2 != 0 and guess.lower == 'odd'):
    print("You guessed odd and your guess is right! You won " + str(bet) + "$!!")
    return +bet
  else:
    print("Your guess was wrong ,Better luck next time! You lost "+str(bet) + "$!!")
    return -bet

#next you and another person pickes card from a desk where higher number of cards win the game
'''def play_card(bet):
  if bet < 0 :
    print('plz bet a positive amount')
    return 0
  if( bet > money ):
    print("Oho!! You don'r have enough money for the bet")
    available_cards = [i*4 for i in range(1,14)]
     
    card1 = available_cards[random.randint(0,len(available_cards)-1)]
    print("Player's card is "+ str(card1))
    available_cards.remove(card1)

    card2 = available_cards[random.randint(0, len(available_cards)-1)]
    print("Opponent's card is"+ str(card2))

  if card1 > card2:
    print("Player wins $"+str(bet)+" with "+ str(card1)+" vs "+str(card2))
    return bet
  if card1 < card2:
    print("Player loses $"+str(bet)+" with "+str(card1)+" vs "+str(card2))
    return -bet
  else:
    print("It is a draw!")
    return 0'''
def play_card(bet):
  #checking for errors and if they have enough money for their bet
  if bet < 0:
    print("Please bet a positive amount")
    return 0
  if bet > money:
      print("Sorry you don't have enough money for that bet!")
      return 0
  #creating list for card values to choose from
  available_cards = list(range(1,14))*4
  available_cards.sort()
  #un-comment blow line to also print all the available cards to check it works
  #print(available_cards)
  #select first card from available cards
  card1 = available_cards[random.randint(0,len(available_cards)-1)]
  print("Player's card is "+str(card1))
  #removes first instance of the already drawn card from available cards
  available_cards.remove(card1)
   #un-comment below line to also print all the available cards to check it works
  #print(available_cards)
  #selects second card from new available cards
  card2 = available_cards[random.randint(0,len(available_cards)-1)]
  print("Opponents card is "+str(card2))
  #checks if player has won and returns cash outcome
  if card1 > card2:
    print("Player wins £"+str(bet)+" with "+str(card1)+" vs "+str(card2))
    print("player win")
    return bet
  if card1 < card2:
    print("Player loses £"+str(bet)+" with "+str(card1)+" vs "+str(card2))
    print("opponent win")
    return -bet
  else:
    print("It is a draw!")
    return 0

   


  




    



#Call your game of chance functions here
print(play_coin_flip('Head', 10))
#print(money)
#print(a)
print(play_card(50))