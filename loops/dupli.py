letters=["A","B","C","D","A"]
unique=set()
for letter in letters:
  if letter in unique:
    print("duplicate: ",letter)
    break
  unique.add(letter)