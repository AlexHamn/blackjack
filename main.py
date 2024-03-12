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
    houseCards = anotherCard(houseCards)
    score = sumArray(houseCards)
    print(f"House cards: {houseCards, score}")
  return score

def bet():
  global chips
  print(f"Remaining chips: {chips}")
  bet = int(input("place your bet"))
  chips = chips - bet
  print(f"Remaining chips: {chips}")
  return bet

def playerTurn():
  bet = bet()
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
      playerScore = sumArray(playerCards)
      playing = False
  
  return playerScore

def payOut(houseScore, playerScore, playerChips, bet):
  if playerScore > 21 or playerScore < houseScore:
    print('you lost :(')
  elif playerScore == 21 and houseScore == 21:
    playerChips += bet
    print('Its a push :l')
  else: 
    playerChips += bet*2
    print('You win! :D')
  return playerChips

def play():
  houseCards = houseCards()
  playerScore = playerTurn()
  houseScore = housePlay()
  results = payOut(houseScore, playerScore, 90, 10)
  print("player chips: " + str(results))
  return chips

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chips = 100

pot = 0

houseStart()