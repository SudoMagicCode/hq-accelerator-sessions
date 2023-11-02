import Lookup


class Output:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        print(f"init of {owner_op}")

    def Start_gen1(self):
        Lookup.GEN.Start_gen_scene()
