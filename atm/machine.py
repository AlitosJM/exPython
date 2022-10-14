from staticmethods.utils import Utils
from datetime import datetime


class Atm(Utils):
    @property
    def get_historical(self):
        return self._historical

    @get_historical.setter
    def set_historical(self, data):
        self._historical.append(data)

    @property
    def get_movement(self):
        return self._countTwo

    @get_movement.setter
    def set_movement(self, mov):
        self._countTwo = mov

    @property
    def get_balance(self):
        return self._balance

    @get_balance.setter
    def set_balance(self, money):
        self._balance = money

    def waiting_for_input(self):
        while self._countOne != 0 and self._wrong is False:
            inputPin = self._get_input()
            if bool(inputPin):
                if inputPin == self._password:
                    print("Welcome, PIN is OK")
                    self._countOne = 0
                    self._wrong = True
                else:
                    self._countOne -= 1
                    print(f"Wrong PIN,you have {self._countOne} chances")
            else:
                self._countOne -= 1
                print(f"Malformed PIN {self._countOne} chances left")
        return inputPin

    def atm_working(self):
        while self._wrong is True:
            options = self._show_input()
            if options == "1":
                print(f"Your balance is: {self.get_balance}")
            elif options == "2":
                money = self._substract_input()
                if money is not None:
                    money = float(money)
                    beforewithDrawn = self.get_balance
                    self.set_balance -= money
                    print(f"Your current balance is: {self.get_balance}")
                    now = datetime.now()
                    self.set_movement += 1
                    data = {
                        'mov': self.get_movement,
                        'date': now.date(),
                        'hour': now.hour,
                        'minute': now.minute,
                        'second': now.second,
                        'lastAmount': beforewithDrawn,
                        'withdrawn': money
                    }

                    self.set_historical = data

                    if self.get_balance <= 0.0:
                        print("Don´t have fundings")
                else:
                    print("Malformed input")
            elif options == "3":
                print("Your movements: ")
                if self.get_balance == 1000.0:
                    print("No movements")
                else:
                    historical = self.get_historical
                    for h in historical:
                        for key, value in h.items():
                            if key in ["hour", "minute", "second"]:
                                print(key+": ", value, end=" ,")
                            else:
                                print(key + ": ", value)
            else:
                print("Wrong option")

            proccesContinue = True
            while proccesContinue is True:
                options = self._continue()
                if options is not None:
                    if options == "X":
                        self._wrong = False
                        proccesContinue = False
                        print("Already finished")
                    else:
                        proccesContinue = False
                        print("Continue")

                else:
                    print("Malformed input. ", "Please, Press C to continue or X to exit", end='\n')
                    proccesContinue = True
