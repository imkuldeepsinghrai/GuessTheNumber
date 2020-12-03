import random 

randNumber = random.randint(1, 100) #--> generating random number 1 to 100
userGuess = None
guesses = 0


while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
	
    #when user guesses it
    if(userGuess==randNumber):
        print("You guessed it right!")

    else:
	#if user enters higher number
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a Lower number")
	#if user enters lower number
        else:
            print("You guessed it wrong! Enter a Higher number")

#how much attempts the user made to guess correct number	
print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
#user breaks the highsocore which is in highscor.txt
if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
