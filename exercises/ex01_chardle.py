__author__ = 730577151

word_input = input("Enter a 5-character word: ")

if len(word_input) != 5:
    print("Word must contain 5 characters")
else: 
    char_input = input("Enter a single character: ") 
    number_of_matches = 0

    if len(char_input) != 1:
        print("Character must be a single character")
    else:
        print("Searching for " + str(char_input) + " in " + str(word_input))

        for n in range (5):
            if str(char_input) == word_input[n]:
                print(str(char_input) + " found at index " + str(n))
                number_of_matches = number_of_matches +1

        if number_of_matches == 1:
            print("there is " + str(number_of_matches) + " instance of " + str(char_input) + " in " + str(word_input))
        else:
            print("there are " + str(number_of_matches) + " instances of " + str(char_input) + " in " + str(word_input))

