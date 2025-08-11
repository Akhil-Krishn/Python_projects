import random
def bot(user_input):
    lst_sps = ["Stone", "Paper" ,"Scissor"]    
    bot = lst_sps[random.randint(0,2)]
    i = "Bot played " 
    if user_input == "Stone" :
        if bot == "Stone" :
            print(i + bot)
            print("tie")
        elif bot == "Paper" :
            print(i + bot)
            print("you lost")
        else:
            print(i + bot)
            print("you win")
    elif user_input == "Paper" :
        if bot == "Stone" :
            print(i + bot)
            print("you win")
        elif bot == "Paper" :
            print(i + bot)
            print("tie")
        else:
            print(i + bot)
            print("you lost")
    elif user_input == "Scissor" :
        if bot == "Stone" :
            print(i + bot)
            print("you lost")
        elif bot == "Paper" :
            print(i + bot)
            print("you win")
        else:
            print(i + bot)
            print("tie")
    elif user_input == "q" :
        quit_input = input("Do you want to quit? y or n : ")
        if quit_input =="y" :
            x = 0
            return x   
    else :        
        print("Invalid input try again")
y = " "
while y != 0 :
    print("Stone Paper and Scissor Game!")        
    userinput = input("Enter Stone, Paper or Scissor and if want to exit press q : ")
    x = bot(userinput)
    y =  x   