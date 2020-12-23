parrot = "Norwegian blue"
print(parrot)
letter = input("what is the letter ")
if letter in parrot.casefold():
    print("Letter is present")
else:
    print("letter is not present")