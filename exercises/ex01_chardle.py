"""EX01 - Chardle - A cute step toward Wordle."""
__author__: str = '730577151'

word_input: str = input("Enter a 5-character word: ")

if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else: 
    char_input: str = input("Enter a single character: ") 
    number_of_matches: int = 0

    if len(char_input) != 1:
        print("Error: Character must be a single character")
        exit()
    else:
        print("Searching for " + str(char_input) + " in " + str(word_input))

        for n in range(5):
            if str(char_input) == word_input[n]:
                print(str(char_input) + " found at index " + str(n))
                number_of_matches = number_of_matches + 1

        if number_of_matches == 1:
            print(str(number_of_matches) + " instance of " + str(char_input) + " found in " + str(word_input))
        elif number_of_matches == 0:
            print("No instances of " + str(char_input) + " found in " + str(word_input))
        else:
            print(str(number_of_matches) + " instances of " + str(char_input) + " found in " + str(word_input))