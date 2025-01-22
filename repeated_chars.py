repeat = []

while True:
  string = input("Enter a string: ").lower()
  if string.isalpha():
    break
  else:
    print('Invalid')

for char in string: 
  if char in repeat:
    print('Repeated character')
  else:
    repeat.append(char)

