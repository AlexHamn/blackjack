import random

def sumArray(array):
  result = 0
  for i in array:
    result += i
  return result

def deal(array):
  array.append(random.choice(cards))
  return array

def housePlay():
  houseCards = []
  houseCards = deal(houseCards)
  houseCards = deal(houseCards)
  score = sumArray(houseCards)
  print(houseCards, score)
  while score < 17:
    houseCards = deal(houseCards)
    score = sumArray(houseCards)
    print(houseCards, score)
  return score

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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chips = 100

pot = 0

print(housePlay())