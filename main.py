import random

def sumArray(array):
  result = 0
  for i in array:
    result += i
  return result

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chips = 100

def deal():
  return random.choice(cards)

def payOut(houseScore, playerScore, chips, bet):
  if playerScore > 21 or playerScore < houseScore:
    print('you lost :(')
  else:
    chips += bet*2
    print('you win! :D')
  return chips

def housePlay(houseCards):
  score = sumArray(houseCards)
  print(houseCards, score)
  while score < 17:
    houseCards.append(deal)
    score = sumArray(houseCards)
    print(houseCards, score)
  return score