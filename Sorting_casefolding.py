pangram = "The quick brown fox jumps over the lazy dog"
print(pangram)
letters = sorted(pangram)
print(letters)
letters1 = sorted(pangram,key=str.casefold)
print(letters1)

