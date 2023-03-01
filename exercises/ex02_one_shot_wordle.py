"""Wordle with One Guess."""
__author__: str = '730577151'

secret_word: str = "python"
word_input = input(f"What is your {len(secret_word)}-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word_input) != len(secret_word):
    word_input = input(f"That was not {len(secret_word)} letters! Try again:")
if word_input != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")

n = 0
result = ''
while n < (len(word_input)):
    if word_input[n] == secret_word[n]:
        result = result + GREEN_BOX
        n = n + 1
    elif word_input[n] in secret_word and word_input[n] != secret_word[n]:
        result = result + YELLOW_BOX
        n = n + 1
    else:
        result = result + WHITE_BOX
        n = n + 1
print(result)