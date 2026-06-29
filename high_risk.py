import time
import random
import func

def highRisk(stavka, balance):
    print("You can choose a number between 0 and 36")
    time.sleep(1)
    print("What'll you choose?")
    time.sleep(1)
    def getNumber():
        while True:
            try:
                type2 = int(input("Write a number: "))
                if type2 in range(0, 37):
                    return type2
                else:
                    print("Wrong answer, try again")
            except ValueError:
                print("Wrong answer, try again")
    type2 = getNumber()
    result = random.randint(0, 36)
    print("Roulette landed on: ", result)
    if type2 == result:
        print(".----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .-----------------.")
        print("| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |")
        print("| |  ____  ____  | || |     ____     | || | _____  _____ | | | | _____  _____ | || |     ____     | || | ____  _____  | |")
        print("| | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| | | ||_   _||_   _|| || |   .'    `.   | || ||_   \|_   _| | |")
        print("| |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | | | |  | | /\ | |  | || |  /  .--.  \  | || |  |   \ | |   | |")
        print("| |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | | | |  | |/  \| |  | || |  | |    | |  | || |  | |\ \| |   | |")
        print("| |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | | | |  |   /\   |  | || |  \  `--'  /  | || | _| |_\   |_  | |")
        print("| |   |______|   | || |   `.____.'   | || |    `.__.'    | | | |  |__/  \__|  | || |   `.____.'   | || ||_____|\____| | |")
        print("| |              | || |              | || |              | | | |              | || |              | || |              | |")
        print("| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' |")
        print("'----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------' ")
        time.sleep(1)
        balance += stavka * 35
        print(f"Your balance: {balance}!!!!!!!!")
        time.sleep(1)
        answer = func.ContorStop()
        if answer == 'continue':
            return ('continue', balance)
    else:
        return func.lose(stavka, balance)

