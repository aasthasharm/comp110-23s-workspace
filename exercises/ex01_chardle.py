__author__ = 730577151

wordInput = input("Enter a 5-character word: ")
charInput = input("Enter a single character: ") 
numberOfMatches = 0

if len(wordInput) != 5:
    print("Word must contain 5 characters")

elif len(charInput) != 1:
    print("Character must be a single character")
else:
    print("Searching for " + str(charInput) + " in " + str(wordInput))

    for n in range (5):
        if str(charInput) == wordInput[n]:
            print(str(charInput) + " found at index " + str(n))
            numberOfMatches = numberOfMatches +1

    if numberOfMatches == 1:
        print("there is " + str(numberOfMatches) + " instance of " + str(charInput) + " in " + str(wordInput))
    else:
        print("there are " + str(numberOfMatches) + " instances of " + str(charInput) + " in " + str(wordInput))

