import random

def sumArray(array):
  result = 0
  for i in array:
    result += i
  return result

def anotherCard(deck, cards):
  deck.append(random.choice(cards))
  return deck

def deal(cards):
  deck = []
  deck.append(random.choice(cards))
  deck.append(random.choice(cards))
  return deck

def houseStart(cards):
  houseCards = deal(cards)
  print(f"House cards: ?, {houseCards[0]}")
  return houseCards

def housePlay(houseCards, cards):
  score = sumArray(houseCards)
  print(f"House cards: {houseCards, score}")
  
  while score < 17:
    print(f"House cards: {houseCards, score}")
    houseCards = anotherCard(houseCards, cards)
    score = sumArray(houseCards)
    print(f"House cards: {houseCards, score}")
  return score

def placeBet(chips):
  print(f"Remaining chips: {chips}")
  while True:
    try:
      bet = int(input("place your bet "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")
  chips = chips - bet
  print(f"Remaining chips: {chips}")
  return bet, chips

def playerTurn(cards, chips):
  bet, chips = placeBet(chips)
  playing = True
  playerCards = deal(cards)
  #print(f"Your cards: {playerCards}")
  extraCard = "n"
  
  while playing:
    playerScore = int(sumArray(playerCards))

    if extraCard == "y":
      playerCards = anotherCard(playerCards, cards)
      print(f"Your cards: {playerCards}")
      playerScore = int(sumArray(playerCards))
    if playerScore > 20 or extraCard == "n":
      print(f"Your cards: {playerCards}")
      playing = False
    extraCard = input("another card?(Y/N)")
    
  
  return playerScore, bet, chips, playerCards

def payOut(houseScore, playerScore, bet, chips):
  if playerScore == 21:
    print("Blackjack! You win!")
    chips += bet * 2
  elif houseScore > 21:
    chips += bet*2
    print('You win! :D')
  elif playerScore > 21 or playerScore < houseScore:
    print('you lost :(')
  elif playerScore == houseScore:
    chips += bet
    print('Its a push :l')
  else: 
    chips += bet*2
    print('You win! :D')
  return chips

def game(chips):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  houseCards = houseStart(cards)
  playerScore, bet, remainingChips, playerCards = playerTurn(cards, chips)
  houseScore = housePlay(houseCards, cards)
  results = payOut(houseScore, playerScore, bet, remainingChips)
  #print(f"Your cards: {playerCards}")
  print("player chips: " + str(results))
  return results

def play():
  chips = 100
  pot = 0
  again = True
  
  while chips > 0:
    chips = game(chips)
  
playerTurn([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 100)
   
#play()