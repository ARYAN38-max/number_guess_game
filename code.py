import random
print("WELCOME TO NUMBER GAME")
number_of_guess = 1
print()
number = random.randint(15,20)
print("NUMBER OF GUESS IS LIMITED TO 9")
while number_of_guess<=9:
    guess_number = int(input("GUESS THE NUMBER:"))
    if guess_number<number:
        print("YOU ENTERED A NUMBER LESS THEN THE ORIGINAL NUMBER")
    elif guess_number>number:
        print("YOU ENTERED THE NUMBER GRATER THEN THE ORIGINAL NUMBER")
    else:
        print("YOU WON")
        print(number_of_guess,"NUMBER OF GUESS YOU TOOK TO COMPLETE THE GAME")
        break
    print(9-number_of_guess,"NUMBER OF GUESSES LEFT")
    number_of_guess = number_of_guess+1
if (number_of_guess>9):
    print("GAME OVER")
    quit()
