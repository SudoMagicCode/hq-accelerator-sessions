import Lookup


class Gen:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        self.MovieTOP = owner_op.op("moviefilein1")
        print(f"init of {owner_op}")

    def Start_gen_scene(self):
        print("starting gen scene")
