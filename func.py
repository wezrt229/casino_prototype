import time
import random
def main_menu():
    while True:
        try:
            time.sleep(1)
            print("1. Roulette")
            print("2. Leave")
            time.sleep(1)
            abc = int(input("Choose what'll you prefer to play: "))
            time.sleep(1)
            if abc == 1:
                print("Roulette? Okay")
                time.sleep(1)
                break
            elif abc == 2:
                print("Goodbye, sir")
                time.sleep(1)
                print("---You've saved your money---")
                exit()
            else:
                print("Wrong answer, try again")
        except ValueError: 
            print("Wrong answer, try again")

def bet(balance):
    while True:
        try:
            stavka = int(input(f"How much will you bet? (Balance: {balance}): "))
            if stavka > balance:
                print(f"You don't have enough money! Your balance is {balance}")
            elif stavka >= 100000:
                print("High stakes")
                balance -= stavka
                return (stavka, balance)
            elif stavka > 0:
                print("Low stakes")
                balance -= stavka
                return (stavka, balance)
            else:
                print("Wrong answer, try again")
        except ValueError:
            print("Wrong answer, try again")
    
def ContorStop():
    print("Choose answer:")
    print("1. Continue")
    print("2. Stop")
    while True:
        try:
            answer = int(input("1 or 2: "))
            if answer == 2:
                    print("---The game ended---")
                    exit()
            elif answer == 1:
                return 'continue'
            else:
                print("Wrong answer, try again")
        except ValueError:
            print("Wrong answer, try again")


def lose(stavka, balance):
    print("Ohh, you lost")
    time.sleep(1)
    print(f"Your balance: {balance}")
    time.sleep(1)
    if balance <= 0:
        print("---You have no money left---")
        time.sleep(1)
        print("---The game ended---")
        exit()
    if stavka >= 100000:
        while True:
            try:
                print("1. Fight")
                print("2. Leave")
                print("3. Return")
                question = int(input("Choose what'll you do: "))
                if question == 1:
                    print("Give me back my money! ")
                    while True:
                        try:
                            print("1. Hit")
                            print("2. Defend")
                            question2 = int(input("Choose what'll you do: "))
                            if question2 in [1 , 2]:
                                print("Get out of here!") 
                                time.sleep(1)
                                print("---You've been kicked out---")
                                time.sleep(1)
                                print("---The game ended---")
                                exit()
                            else:
                                print("Wrong answer, try again")
                        except ValueError:
                                print("Wrong answer, try again")
                elif question == 2:
                    print("---You lost---")
                    time.sleep(1)
                    print("---The game ended---")
                    exit()
                elif question == 3:
                    return ('continue', balance)
                else:
                    print("Wrong answer, try again")
            except ValueError:
                    print("Wrong answer, try again")
    else:
        return (ContorStop(), balance)
        

def Cont():
    while True:
        try:
            print("Do you want to continue?")
            time.sleep(1)
            print("1. Yes")
            print("2. No")
            time.sleep(1)
            cont = int(input("Choose an answer: "))
            if cont == 1:
                return cont
            elif cont == 2:
                return cont
            else:
                print("Wrong answer, try again")
        except ValueError:
            print("Wrong answer, try again")

def wiN(stavka, balance):
    print("You won!!!")
    time.sleep(1)
    balance += stavka * 2
    print(f"Your balance: {balance}")
    time.sleep(1)
    return balance

def rand_choice(options):
    time.sleep(1)
    print("Let's play")
    result = random.choice(options)
    print("Result:", result)
    return result