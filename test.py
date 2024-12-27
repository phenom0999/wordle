
# Set lists and dictionary
available_words = []
correct = []
incorrect = []
dump = []
used_letters = []
position = {
    0 : "",
    1 : "",
    2 : "",
    3 : "",
    4 : "",
}

anti_position = {
    0 : "",
    1 : "",
    2 : "",
    3 : "",
    4 : "",
}


# function that guesses a word
def get_guess():

    if len(dump) == 0:
        return "trace"
    if len(dump) == len(available_words):
        return None
    i = 0
    for word in available_words:
        if i not in dump:
            guess = available_words[i]
            dump.append(i)
            dump.sort()
            break
        i = i + 1  

    return guess

# Read the file and store all the words in a list
with open("words.txt", "r") as words_file:
    for line in words_file:
        for word in line.strip().split("\n"):
            available_words.append(word)

# Print initial guess
guess = get_guess()
print(guess)

keep_running = True

# Infinite loop
while keep_running:

    # Get info about letters and positions
    i = 0
    for letter in guess:
        weight = int(input(letter + " : " ))
        if weight == 0:
            if letter in used_letters:
                continue
            incorrect.append(letter)
        if weight == 1:
            if letter in incorrect:
                incorrect.remove(letter)
            anti_position[i] = letter
            correct.append(letter)
        if weight == 2:
            if letter in incorrect:
                incorrect.remove(letter)
            position[i] = letter
            correct.append(letter)
        used_letters.append(letter)
        i = i + 1

    # Remove all words containing letters in incorrect
    i = 0
    for word in available_words:
        if i not in dump:
            for letter in word:
                if letter in incorrect:
                    dump.append(i)
                    if word == "plume":
                        print("1st one")
                    dump.sort()
                    break
        i = i + 1
    
    # Remove all words which don't have letters present in correct
    i = 0
    for word in available_words:
        if i not in dump:
            for letter in correct:
                if letter not in word:
                    dump.append(i)
                    if word == "plume":
                        print("2nd one")
                    dump.sort()
                    break
        i = i + 1

    # Remove all words which don't have correct letter in correct position (green)
    i = 0
    for x in position.values():
        if x != "":
            j = 0
            for word in available_words:
                
                if j not in dump:
                    if word[i] is not x:
                        dump.append(j)
                        if word == "plume":
                            print("3rd one")
                        dump.sort()
                j = j + 1
        i = i + 1

    # Remove all words which have correct letter in incorrect position (yellow)
    for x in anti_position.values():
        if x != "":
            j = 0
            for word in available_words:
                if j not in dump:
                    if word[i] is x:
                        dump.append(j)
                        if word == "plume":
                            print("4th one")
                        dump.sort()
                j = j + 1
        i = i + 1

    # Print guesses
    next_word = "y"
    while next_word == "y":
        guess = get_guess()
        if guess == None:
            print("No words availabe")
            keep_running = False
            break
        print(guess)
        next_word = input("Give alternate word? (y/n) -> ")
    
    
    '''i = 0
    for word in available_words:
        if i not in dump:
            print(word)
        i = i + 1'''

