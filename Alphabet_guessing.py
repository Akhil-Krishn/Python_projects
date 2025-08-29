import random
import string 
import time
print("Alphabet guessing game")
running = True
while running:
    time.sleep(0.5)
    global x
    x = True
    alphabets = list(string.ascii_lowercase)
    idiot_text = "why did you type a number you idiot!!, try again!!"
    idiot_text = idiot_text.upper()
    alphabet_random = alphabets[random.randint(0,25)]
    alphabet_input = input("Enter a lower case alphabet here(without spaces) ")
    if alphabet_random == alphabet_input :
        print("The alphabet was " + alphabet_random)
        print("WHAT! wow, you won, you are the lucky 1 in 26 winner...Good Job!")
        lol = True
        while lol:
            quit_input = input("do you want to quit? y/n ")
            if quit_input == "y":
                running = False
                lol = False
            elif quit_input == "n":
                lol = False
                continue
            else :
                print("invalid input, try again")
    elif (len(alphabet_input)) > 1 :
        print("invalid input, try again")
    else:
        try: 
            int(alphabet_input)
            print(idiot_text)
            x = False
        except:
            x = True
        if x is True:
            print("The alphabet was " + alphabet_random)
            print("oohh sorry try again")
            lol = True
            while lol:
                quit_input = input("do you want to quit? y/n ")
                if quit_input == "y":
                    running = False
                    lol = False
                elif quit_input == "n":
                    lol = False
                    continue
                else :
                    print("invalid input, try again")