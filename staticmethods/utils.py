import re


class Utils:
    _password = "1235"
    _wrong = False
    _countOne = 3
    _countTwo = 0
    _balance = 1000.0
    _historical = []

    @staticmethod
    def _get_input():
        pin = input("\n Enter 4 Digits Pin code please: \n")

        if pin.isdigit():
            r = re.findall('^[0-9]{4}$', pin)
            if r:
                return r.pop()
        return None


    @staticmethod
    def _show_input():
        print("Menu: ", "Press 1 to show balance", "Press 2 to withdrawn", "Press 3 to get the last movement", sep="\n")
        pin = input("\n  Enter an option please: \n")
        if pin.isdigit():
            r = re.findall('^[1-3]{1}$', pin)
            if r:
                return r.pop()
        return None

    @staticmethod
    def _substract_input():
        print("Menu: ", "Withdrawning", sep="\n")
        pin = input("\n  Getting funding: \n")
        if pin.isdigit():
            r = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", pin)
            if r:
                return r.pop()
        return None

    @staticmethod
    def _continue():
        print("Press C to continue or X to exit", sep="\n")
        pin = input("\n  Enter an option please: \n")
        if pin.isalpha():
            r = re.findall("[C|X]", pin)
            if r:
                return r.pop()
        return None

    @staticmethod
    def exit(msg="Time's up!!"):
        print(msg)
