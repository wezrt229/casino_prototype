import time
import random
import func

def red_black(stavka, balance):
    while True:
        try:
            print("What do you want to bet on?")
            time.sleep(1)
            print("1. Red")
            print("2. Black")
            bet1 = int(input("1 or 2: ")) 
            if bet1 == 1:
                result = func.rand_choice(["Red", "Black"])
                if result == "Red":
                    balance = func.wiN(stavka, balance)
                    answer = func.ContorStop(balance)
                    if answer == 'continue':
                        return ('continue', balance)
                else:
                    return func.lose(stavka, balance)
            elif bet1 == 2:
                result = func.rand_choice(["Red", "Black"])
                if result == "Black":
                    balance = func.wiN(stavka, balance)
                    answer = func.ContorStop(balance)
                    if answer == 'continue':
                        return ('continue', balance)
                else:
                    return func.lose(stavka, balance)
            else:
                print("Wrong answer, try again")
        except ValueError:
            print("Wrong answer, try again")   

def even_odd(stavka, balance):           
    while True:
        try:
            print("What do you want to bet on?")
            time.sleep(1)
            print("1. Even")
            print("2. Odd")
            bet2 = int(input("1 or 2: ")) 
            if bet2 == 1:
                result = func.rand_choice(["Even", "Odd"])
                if result == "Even":
                    balance = func.wiN(stavka, balance)
                    answer = func.ContorStop(balance)
                    if answer == 'continue':
                        return ('continue', balance)
                else:
                    return func.lose(stavka, balance)
            elif bet2 == 2:
                result = func.rand_choice(["Even", "Odd"])
                if result == "Odd":
                    balance = func.wiN(stavka, balance)
                    answer = func.ContorStop(balance)
                    if answer == 'continue':
                        return ('continue', balance)
                else:
                    return func.lose(stavka, balance)
            else:
                print("Wrong answer, try again")
        except ValueError:
            print("Wrong answer, try again")

def lowRisk(stavka, balance):
    time.sleep(1)
    print("What type of bet you want to do?")
    time.sleep(1)
    while True:
        try:
            print("1. Red or Black")
            print("2. Even or Odd")
            time.sleep(1)
            type1 = int(input("1 or 2: "))  
            if type1 == 1:                 
                return red_black(stavka, balance)  
            elif type1 == 2:
                return even_odd(stavka, balance)
            else:
                print("Wrong answer, try again")
        except ValueError:
                print("Wrong answer, try again")