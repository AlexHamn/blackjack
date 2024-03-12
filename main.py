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

def housePlay():
  houseCards = deal()
  score = sumArray(houseCards)
  print(houseCards, score)
  while score < 17:
    houseCards = deal(houseCards)
    score = sumArray(houseCards)
    print(houseCards, score)
  return score

def playerTurn():
  playerCards = deal()

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
  houseScore = housePlay()
  playerScore = 18
  results = payOut(houseScore, playerScore, 90, 10)
  print("player chips: " + str(results))

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chips = 100

pot = 0

print(play())