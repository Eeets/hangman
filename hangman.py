def hangman(word):
    wrong = 0
    stages = ["",
              "__________         ",
              "|                  ",
              "|        |         ",
              "|        0         ",
              "|       /|\        ",
              "|       / \        ",
              ]
    remaining_letters = list(word)
    board = ["-"] * len(word)
    win = False
    print("Welcome to Hangman!")
    print(" ".join(board))
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter "
        char = input(msg)
        if char in remaining_letters:
            while char in remaining_letters:
                cind = remaining_letters.index(char)
                board[cind] = char
                remaining_letters[cind] = "*"
        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "-" not in board:
            print("You win!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print(f"You lose!  It was {word}")

hangman("bailey")

            
