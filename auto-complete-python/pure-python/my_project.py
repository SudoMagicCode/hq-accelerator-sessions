"""
SudoMagic | sudomagic.com
Authors | Matthew Ragan, Ian Shelanskey
Contact | contact@sudomagic.com
"""

import example
from newLib import myUtils
import newLib


def Foo(arg1: int) -> float:
    # our code does something here
    new_val: float = arg1 + 0.125
    return new_val


# using a function from a single file
my_val = example.FooFoo(3)

# from a library
now = myUtils.get_current_time()
print(now.day)

my_str = newLib.BarBar(1.0, "hello")

myFlipFlop = newLib.FlipFlop()

myFlipFlop.add_flips(5)
