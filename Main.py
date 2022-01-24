import time



class LVLing():
    def __init__(self):
        # VAR
        self.credits = 0
        # Const
        self.exercise_cost = {"Отжимание"   : 1,
                              "Приседание"  : 0.5,
                              "Подтягивание": 2,   }

    def begin(self):
        print("""
─────────────────────────────────
─────╔╗───────────╔╗─────────────
─────║║───────────║║─────────────
─────║║──╔══╦╗╔╦══╣║╔╦═╗╔══╗─────
─────║║─╔╣║═╣╚╝║║═╣║╠╣╔╗╣╔╗║─────
─────║╚═╝║║═╬╗╔╣║═╣╚╣║║║║╚╝║─────
─────╚═══╩══╝╚╝╚══╩═╩╩╝╚╩═╗║─────
────────────────────────╔═╝║─────
────────────────────────╚══╝─────
─────────────────────────────────
""")
        self.status()
        print("Choose action")
        print("1: Do exercise")
        print("2: Negative action")
        print("3: Get status")
        print("4: quit")
        while True:
            inp = int(input())
            if   inp == 1:
                self.do_exercise()
            elif inp == 2:
                x = int(input("Enter number: "))
                self.credits += x
                print("Credits + "+str(x))
                print("Total: " + str(self.credits))
            elif inp == 3:
                self.status()
            elif inp == 4:
                break


    def status(self):
        print("Your credits:", self.credits)


    def do_exercise(self):
        print("Not found")





if __name__ == "__main__":
    LvL = LVLing()
    LvL.begin()

