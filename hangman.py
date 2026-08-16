import random
import time

category_descriptions = {
    "animals": "Creatures from the animal kingdom.",
    "countries": "Nations from around the world.",
    "games": "Popular video games."
}

categories= {"animals":["PANDA","LION","GIRAFFE","ELEPHANT"],
            "countries":["INDIA","JAPAN","BRAZIL"],
            "games":["MINECRAFT","VALORANT","ROBLOX","FORTNITE"]}

difficulties ={"easy":8,
               "medium":6,
               "hard":4}


def typewriter(text,delay=0.06):
    for character in text:
        print(character,end="",flush=True)
        time.sleep(delay)
    print()



while True:

    typewriter("Whats your name O Great Sire!")
    name=input("")

    while True:
        print("Choose your difficulty level Sire",name,"\neasy,medium or hard")
        difficulty=input().strip().lower()

        if difficulty in difficulties:
            lives=difficulties[difficulty]
            break
        print("That difficulty does not exist O Great Dumb Sire",name,"\nTry again")

    while True:

        typewriter("Enter the category you wish the word to be from:")
        typewriter("animals")
        typewriter("countries")
        typewriter("games")

        category=input().strip().lower()

        if category in categories:
            break

        typewriter("That category does not exist idiot.\nTRY AGAIN")

    secret_word = random.choice(categories[category])

    print(f"\nCategory: {category.title()} - {category_descriptions[category]}")
    print(f"Difficult:{difficulty.title()}|Lives:{lives}")

    guessed_letters=[]
    won=False


    while lives>0:

        guess=input("Guess the letter ").strip().upper()

        if len(guess)!=1 or not guess.isalpha():
            typewriter("Oiiiiiii mister i told to guess a letter.Not a GODDAMNN WORD OR NUMBER 	>:[")
            continue

        if guess in guessed_letters:
            typewriter("You already guessed this letterrrr ughhhhhh. \n Try another one dude")
            continue

        guessed_letters.append(guess)
        if guess not in secret_word:
            lives -=1
            print("Remaining lives:",lives)


        for letter in secret_word:
            if (letter in guessed_letters):
                print(letter,end=" ")
            else:
                print("_",end=" ")
        print()

        if all(letter in guessed_letters for letter in secret_word):
            won=True
            typewriter("NOOOO WAYYYYY!!")
            typewriter("YOU ACTUALLY GUESSED THE WORD")
            typewriter("HMMMMM ALRIGHT YOUR WIN I GUESS HMPH (  •̀ ⤙ •́  )")
            break
            

    print()
    if lives==0:
        print("Game over lol! The word was:", secret_word,";)")
        won=False

    play_again=input("Play again▶️? (yes/no): ").strip().lower()

    if play_again != "yes":
        break


