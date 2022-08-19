from vectors import vector

from random import randint, uniform


class brain():



    def __init__(self, nMoves, inst = " "):

        self.instructions = []

        self.nMoves = nMoves
        self.mutationRate = 0.01

        if isinstance(inst,list):

            self.instructions = inst

            assert (len(self.instructions) == self.nMoves), "Instruction length longer than nMoves"
        else:

            self.rndInstructions()

    def __str__(self):

        return(f"Brain type with {self.nMoves} instructions")

    def __repr__(self):

        return f"Brain:{self.nMoves}, id:{id(self)}\n"


    def rndInstructions(self):

        for i in range(self.nMoves):

            self.instructions.append(vector.make2D(randint(0, 360)))

    def mutate(self):

        for i in range(len(self.instructions)):

            if uniform(0,1)<self.mutationRate:

                self.instructions[i] = vector.make2D(randint(0, 360))


def main():

   tst1 = brain(100)

   tst1.rndInstructions()

   tst2 = brain(len(tst1.instructions),tst1.instructions)

   tst2.mutate()

   print(tst2)





if __name__ == "__main__":
    main()