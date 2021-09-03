from vectors import vector
from random import randint

class brain():


    def __init__(self, nMoves, inst = " "):
        self.instructions = []
        self.nMoves = nMoves
        if isinstance(inst,list):
            self.instructions = inst
            assert (len(self.instructions) == self.nMoves), "Instruction length longer than nMoves"
        else:
            self.rndInstructions()


    def rndInstructions(self):
        for i in range(self.nMoves):
            self.instructions.append(vector.make2D(randint(0, 360)))


def main():
   tst1 = brain(100)
   tst1.rndInstructions()
   tst2 = brain(100,tst1.instructions)




if __name__ == "__main__":
    main()