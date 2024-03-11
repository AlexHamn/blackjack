import random

def sumArray(array):
  result = 0
  for i in array:
    result += i
  return result

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chips = 100

def deal(array):
  array.append(random.choice(cards))
  return array

def payOut(houseScore, playerScore, chips, bet):
  if playerScore > 21 or playerScore < houseScore:
    print('you lost :(')
  else:
    chips += bet*2
    print('you win! :D')
  return chips

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

print(housePlay())