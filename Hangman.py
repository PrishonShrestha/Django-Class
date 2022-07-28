def Hangman():
        user_input = str(input("Enter a word: "))
        print("Word length: ", len(user_input))
        word = [x for x in user_input]

        correct_input =[]
        incorrect_input = []
        #print(word)

        
        while len(correct_input) != len(word):
            if len(incorrect_input) != 5:
                player_guess = str(input("Guess a letter: "))
                #for player_guess in word:
                if player_guess in word:
                    print("Correct")
                    if player_guess not in correct_input:

                        c=word.count(player_guess)
                        for i in range(0,c):  #Insert duplicate letters
                            correct_input.append(player_guess)
                        print("Correct Guesses: ", correct_input)

                    else:
                        print("Already guessed")
                else:
                    print("Incorrect")
                    if player_guess not in incorrect_input:
                        incorrect_input.append(player_guess)
                        #print("Incorrect Guesses: ", len(incorrect_input))
                        print("Number of guesses left: ", (5-len(incorrect_input)))
                    else:
                        print("Already guessed")
            else:
                print("         Game over")
                print( "         _____________")
                print( "         !           |")
                print( "      |0   0|        |")
                print( "         |           |")
                print( "        /|\          |")
                print( "       / | \         |")
                print( "         |           |")
                print( "        / \          |")
                print( "       /   \         |")
                print( "                     |")
                break
        else:
            print("Congratulation")
            print(user_input)



Hangman()