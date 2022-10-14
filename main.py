# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import staticmethods.utils
from staticmethods.utils import Utils
from atm.machine import Atm

import time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    atm = Atm()
    print("Enter your PIN code")
    #t = Timer(1, Utils.exit, args=("Time's up!!",))
    #t.start()

    inputCheck = atm.waiting_for_input()
    atm.atm_working()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
