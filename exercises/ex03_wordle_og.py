"""Wordle with One Guess."""
__author__: str = '730577151'

secret_word: str = "python"
word_input = input(f"What is your {len(secret_word)}-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(string_searched: str,char_searching: str) -> bool:
    """True if the character is in the first string at any index and false otherwise."""
    assert len(char_searching) == 1
    idx: int = 0
    while idx < len(string_searched):
        if string_searched [idx] == char_searching [0]:
            return True
        idx = idx + 1
    return False

def emojified(guess: str, secret_word: str) -> str:
    """Returns appropriate emoji for char in string."""
    assert len(guess) == len(secret_word)
    idx: int = 0
    emoji_str: str = ""
    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            emoji_str = emoji_str + GREEN_BOX   
        elif contains_char(secret_word, guess[idx]):
            emoji_str = emoji_str + YELLOW_BOX
        else:
            emoji_str = emoji_str + WHITE_BOX
        idx = idx + 1
    return emoji_str

def input_guess(expected_len: int) -> str:
    guess: str = str(input(f"Enter a {expected_len} character word: "))
    while len(guess) != expected_len:
        guess = str(input(f"That wasn't {expected_len} chars! Try again: "))
    return guess

def main() -> None:
    """Main loop of the program and main loop of the game."""
    secret_word: str = "codes"
    guess: str = ""
    emoji_str: str = ""
    cur_turn: int = 1
    total_turns = 6
    game_win: bool = False
    while (cur_turn <= total_turns and game_win is False):
        print(f"=== Turn {cur_turn}/{total_turns} ===")
        guess = input_guess(len(secret_word)) 
        print(emojified(guess,secret_word))
        if guess == secret_word:
            game_win = True
        else:
            cur_turn = cur_turn + 1
    if game_win == True:
        print(f"You won in {cur_turn}/{total_turns} turns!")
    else:
        print((f"X/{total_turns} - Sorry, try again tomorrow!"))

if __name__ == "__main__":
    main()
