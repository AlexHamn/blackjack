import random

def sumArray(array):
  result = 0
  for i in array:
    result += i
  return result

def anotherCard(deck):
  deck.append(random.choice(cards))
  return deck

def deal():
  deck = []
  deck.append(random.choice(cards))
  deck.append(random.choice(cards))
  return deck

def houseStart():
  houseCards = deal()
  print(f"House cards: ?, {houseCards[0]}")
  return houseCards

def housePlay(houseCards):
  houseCards = houseCards
  score = sumArray(houseCards)
  
  while score < 17:
    print(f"House cards: {houseCards, score}")
    houseCards = anotherCard(houseCards)
    score = sumArray(houseCards)
    print(f"House cards: {houseCards, score}")
  return score

def placeBet():
  global chips
  print(f"Remaining chips: {chips}")
  bet = int(input("place your bet"))
  chips = chips - bet
  print(f"Remaining chips: {chips}")
  return bet, chips

def playerTurn():
  bet, chips = placeBet()
  playing = True
  playerCards = deal()
  print(playerCards)
  extraCard = input("another card?(y/n)")
  
  while playing:
    if extraCard == "y":
      playerCards = anotherCard(playerCards)
      playerScore = sumArray(playerCards)
      print(f"Your cards: {playerCards}")
      extraCard = input("another card?(Y/N)")
    else:
      playerScore = int(sumArray(playerCards))
      playing = False
  
  return playerScore, bet, chips

def payOut(houseScore, playerScore, bet, chips):
  if houseScore > 21:
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

def play():
  houseCards = houseStart()
  playerScore, bet, chips = playerTurn()
  houseScore = housePlay(houseCards)
  results = payOut(houseScore, playerScore, bet, chips)
  print("player chips: " + str(results))
  return chips

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chips = 100

pot = 0

play()