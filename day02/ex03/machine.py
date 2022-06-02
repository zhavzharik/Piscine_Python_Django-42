from beverages import *
import random


class CoffeeMachine:
    def __init__(self):
        self.name = "coffeeMachine"
        self.count = 0
        self.is_fixed = True

    class EmptyCap(HotBeverage):
        def __init__(self):
            super().__init__()
            self.price = 0.90
            self.name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."
            super().__init__(self.message)

    def repair(self):
        self.is_fixed = True

    def serve(self):
        if not self.is_fixed:
            raise self.BrokenMachineException()
        beverages = [Coffee(), Tea(), Chocolate(), Cappuccino(), self.EmptyCap()]
        choice = random.randint(0, 4)
        parameter = beverages[choice]
        self.count += 1
        if self.count == 10:
            self.count = 0
            self.is_fixed = False
        return parameter


def test():
    machine = CoffeeMachine()
    for i in range(38):
        try:
            beverages = machine.serve()
            print(beverages)
        except machine.BrokenMachineException as e:
            print(e)
            machine.repair()


if __name__ == '__main__':
    test()
