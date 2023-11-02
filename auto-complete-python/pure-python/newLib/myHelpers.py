
def BarBar(arg1: float, arg2: str) -> str:
    """This is a doc string
    """
    return f"{arg1} is a {arg2}"


class FlipFlop:
    """This is a doc string for your class
    """

    def __init__(self):
        self.numFlips = 5
        self.numFlops = 10

    def add_flips(self, num_flips: int) -> int:
        """The number of flips to add
        """
        self.numFlips += num_flips
        return self.numFlips
