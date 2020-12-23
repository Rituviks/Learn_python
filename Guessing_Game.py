Answer = 5
print("Guess a number:")
Guess = int(input())
if Guess < Answer:
    print("Guess higher by {}".format(Answer-Guess))

elif Guess == Answer:
    print("You got it")
else:
   print("Guess lower by {}".format(Guess-Answer))
