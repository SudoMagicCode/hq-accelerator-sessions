"""
SudoMagic   | sudomagic.com
Authors     | Matthew Ragan
Contact     | 
"""

# td python mods
import Lookup
import scene


class Gen:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        self.MovieTOP = owner_op.op("moviefilein1")
        self.Scene1: Scene.Scene = owner_op.op("base_scene1")
        self.Scene1: Scene.Scene = owner_op.op("base_scene2")
        print(f"init of {owner_op}")

    def Start_gen_scene(self):
        print("starting gen scene")
