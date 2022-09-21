#Hangman by: Ithamar Baron [21/09/22]
def Hang_Man_Stage(key):
    """this function is responsible for the hangman stages
    :param key: a key used to pick a stage from the dict
    :return: returning the corresponding stage (string)
    """
    hang_man_stages = {
        0: "x-------x",
        1: """
        x-------x
        |
        |
        |
        |
        |""",
        2: """
        x-------x
        |       |
        |       0
        |
        |
        |""",
        3: """
        x-------x
        |       |
        |       0
        |       |
        |
        |""",
        4: r"""
        x-------x
        |       |
        |       0
        |      /|\
        |
        |""",
        5: r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      /
        |""",
        6: r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |"""
    }
    return hang_man_stages[key]

def Hang_Man_Title():
    """this function prints the HANGMAN title and the amount of tries"""
    print(r""" 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/""")
    print("You got [6] tries!")

def is_valid_input(letter):
    """This function is responsible for validating the user input
    :param letter: input from the user (String)
    :return: allowed char or not (Bool)"""
    if (not letter.isalpha() or len(letter) > 1):
        return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """This function is responsible for showing the user which letters he got right out of the secret word
    :param secret_word: (String) the secret word selected from the file
    :param  old_letters_guessed: (List) of letters the user guessed
    :return output: (String) presents the user's progress
    """
    output = ""
    for char in secret_word:
        if char in old_letters_guessed:
            output+= char+" "
        else:
            output+= "_ "
    return output

def check_win(secret_word, old_letters_guessed):
    """This function is responsible for checking if the user got the word right
    :param secret_word: (String) the secret word selected from the file
    :param  old_letters_guessed: (List) of letters the user guessed
    :return (bool): if he got it right [True] else [False]"""
    count = 0
    for i in secret_word:
        if i in old_letters_guessed:
            count += 1
    return count == len(secret_word)

def choose_word(file_path, index):
    """This function is responsible for picking the secret word
    :param file_path : (String) it's the path to a text file containing the words
    :param index: (int) choosing which word to use from the file
    :return (String): the selected word from the file
    """
    file = open(file_path, 'r').read().split(" ")
    lenght_of_file = len(file) - 1
    if index > lenght_of_file:
        return file[index % len(file)]
    else:
        return file[index]

def Is_In_List(letter, old_letters_guessed):
    if (letter in old_letters_guessed):
        return True
    return False


def main():
#vars
    secret_word = ""
    old_letters_guessed = []
    MAX_TRIES = 6
    num_of_tries = 0
#initialization
    Hang_Man_Title()
    file_path = input("Enter file path:")
    word_number = int(input("Enter index: "))
    secret_word = choose_word(file_path,word_number)
    print("Let’s start!")

    print(Hang_Man_Stage(num_of_tries))
    print(show_hidden_word(secret_word, old_letters_guessed))
#Game Loop
    while MAX_TRIES > num_of_tries and not check_win(secret_word, old_letters_guessed):
        guess = str(input("Guess a letter:"))
        guess = guess.lower()
        while(not is_valid_input(guess)): #this part will keep looping until the input is valid
            print("X")
            guess = str(input("Guess a letter:"))
            guess = guess.lower()

#if guess is correct but already in the list
        if (Is_In_List(guess,old_letters_guessed)):
            print("X")
            print(old_letters_guessed)

#if guess is correct
        elif (guess in secret_word):
            old_letters_guessed.append(guess)
            print(show_hidden_word(secret_word, old_letters_guessed))

#if guess is incorrect
        else:
            old_letters_guessed.append(guess)
            print(":(")
            num_of_tries = num_of_tries + 1
            print(Hang_Man_Stage(num_of_tries))
            print(show_hidden_word(secret_word,old_letters_guessed))

#The game has ended now we determent the result
    if(check_win(secret_word,old_letters_guessed)):
        print("=================")
        print("    YOU WON! ")
        print("=================")
    else:
        print("=================")
        print("   YOU LOSE! ")
        print("=================")

if __name__ == "__main__":
    main()
























