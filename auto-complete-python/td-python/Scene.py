"""
SudoMagic   | sudomagic.com
Authors     | Matthew Ragan
Contact     | 
"""


class Scene:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        print(f"init of {owner_op}")

    def Start_scene(self):
        print("starting scene")
