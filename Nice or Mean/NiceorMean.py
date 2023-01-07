#   This is the Nice or Mean Game
#   Python 3.11.1
#   Carolina Espinosa



def start(nice=0,mean=0,name=""):
    #get user's name
    name = desc_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

    

def desc_game(name):
    """
        check if this is a new game or not
        if it's new, get the user's name
        if it's not , thank the player for
        playing aagain and cont w the game
    """
    #if we don't already have the user's name
    #they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome {}".format(name))
                    import time
                    time.sleep(2)#added time delay to slow down the program for better readability
                    print("\nIn this game you will be greeted \nby different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions")
                    stop = False
    return name




def nice_mean(nice,mean,name):
    import time#added time delay to slow down the program for better readability
    time.sleep(1.5)
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for conversation, will you be nice \nor mean? (N/M \n>>>)").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)#pass the 3 vars to the score
    



def show_score(nice,mean,name):
    import time#added time delay to slow down the program for better readability
    time.sleep(1.5)
    print("\n{}, your current total: \n({} Nice and {} Mean)".format(name,nice,mean))



def score(nice,mean,name):
    #score func is being passed the values stored within the 3 vars
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


#this defines what happens when there's a W or an L
def win(nice,mean,name):
    print("\nNice job {}, you win!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nOh no {}! You lose".format(name))
    again(nice,mean,name)




def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you wanna play again? (y/n): ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for YES, (N) for NO:\n>>>")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)






if __name__ == "__main__":
    start()
