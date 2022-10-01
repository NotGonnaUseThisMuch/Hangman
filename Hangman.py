import random
name = input("Hello! What is your name?")
print("Ok, good luck", name)
word_list = ['red', 'blue', 'minecraft', 'hulk', 'english', 'football', 'block', 'rainbow', 'computer', 'science', 'programming',
'python', 'mathematics', 'player', 'condition',
'reverse', 'water', 'board', 'garden', 'football', 'gaming', 'tennis', 'fire', 'ice', 'thor', 'birthday', 'captain', 'tolerate' ]
word = random.choice(word_list)
print("This is hangman, so try to guess the word. You have 12 tries")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")

            failed += 1
    if failed == 0:
        print("You win!! Congratulations :)")
        print("The word was:", word)
        break
    guess = input("Guess a character")
    guesses += guess

    if guess not in word:
              turns -= 1
              print('Wrong')
              print("You have", + turns, "more guesses")

              if turns == 0:
                print("You lose. Get rekt ._.")     