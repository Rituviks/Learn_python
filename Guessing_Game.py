import random
highest = 1000
Answer = random.randint(1,highest)
print(Answer)
print("Guess a number:")
Guess = 0
while Guess != Answer:
    Guess = int(input())
    if Guess < Answer:
        print("Guess higher by {}".format(Answer-Guess))

    elif Guess == Answer:
        print("You got it")
    else:
       print("Guess lower by {}".format(Guess-Answer))
