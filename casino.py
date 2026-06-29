import random
import time
import func
import low_risk
import high_risk

print("-------WELCOME TO CASINO-------")
time.sleep(1)
print("Here is what you can play:")
func.main_menu()
balance = 100000
ContOrStop = func.ContorStop()
while ContOrStop in ['continue']:
    stavka, balance = func.bet(balance)
    print("Risks:")
    time.sleep(1)
    while True:
        try:
            print("1. Low risk")
            print("2. High risk")
            time.sleep(1)
            ris = int(input("What'll you choose? : "))
            if ris == 1:
                    ContOrStop, balance = low_risk.lowRisk(stavka, balance)
                    break
            elif ris == 2:
                    ContOrStop, balance = high_risk.highRisk(stavka, balance)  
                    break
            else:
                  print("Wrong answer, try again") 
        except ValueError:
              print("Wrong answer, try again")
                     