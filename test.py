#While Loop

def main():
  counter = 0
  while counter != 10:
    counter += 1
    print "The counter has not reached 10."
#main()

def fruit():
  fruitGuess = ""
  while fruitGuess != "apple":
    fruitGuess = raw_input("Guess McDonough's favorite fruit:")
  print "You guessed McDonough's fruit correctly! It is an apple."
#fruit()

def inception():
  totalRuns = input("How many times do you want to run this program?")
  for i in range(totalRuns):
      fruitVariable = ""
      while fruitVariable != "apple":
        fruitVariable = raw_input("Guess McDonough's favorite fruit:")
      print "You guessed McDonough's fruit correctly! It is an apple."
#inception()

def number():
    numberGuess = int
    while numberGuess != -1:
        numberGuess = input("Guess the number. It is between -10 and 10:")
    print "You guessed the number! It was -1."
#number()

def continuedRunProgram():
    continueRunning = True
    numberGuess = int
    while continueRunning != False:
        while numberGuess != -1:
            numberGuess = input("Guess the number. It is between -10 and 10:")
        print "You guessed the number! It was -1."
        continueRunning = input("Would you like to run this program again? Type True for yes, or anything else for no.")
continuedRunProgram()      