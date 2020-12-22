Name = input("what is your name ?")
age = int(input("How old are you ,{0}".format(Name)))
print(age)

if age < 18:
    print(" Sorry you can vote after {0} year".format(18-age))
elif age == 900:
    print("Is that a age")
else:
    print("You can vote")





