#WordCount.py
#Name:Addy Duering
#Date:3/1/26
#Assignment:Lab 6

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount = lineCount + 1
    #print(line)
    words = line.split()
    wordCount = wordCount + len(words)
    letterCount = letterCount + len(line)
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)

if __name__ == '__main__':
  main()
