count = 0

repeat = []

alpha = "abcdefghijklmnopqrstuvwxyz"

def find_repeated(words):

    global count
    
    for char in words:
        if char in repeat:
            print("Repeated characters")
            break
        repeat.append(char)

        if char in alpha:
            count += 1
            if count > 2:
                print("Repeated characters")
                break


string = input("Enter a string: ").lower()

find_repeated(string)

print(repeat)
