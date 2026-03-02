#DiceRoll.py
#Name:Addy Duering
#Date:3/1/26
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0] #2-12
  #Create two dice values ranging from 1 - 6 each
  for r in range(1000):
    dice1 = random.randint(1,6)
    rolls[dice1 - 1] = rolls[dice1 - 1] + 1
    dice2 = random.randint(1,6)
    rolls[dice2 - 1] = rolls[dice2 - 1] + 1
    total = dice1 + dice2
    rolls[total - 2] = rolls[total - 2] + 1
  
  #print   total = dice1 + dice2
  rolls[total - 2] = rolls[total - 2] + 1
  #print statistics for dice rolls
  dice = 2
  for count in rolls:
    print(dice, ":", count) 
    dice = dice + 1

if __name__ == '__main__':
  main()
