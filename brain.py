from vectors import vector
from random import randint

class brain():

    @classmethod
    def fromList(cls, l):
        tmpB = cls(l.length)
        tmpB.instructions = l
        return(tmpB)

    def __init__(self, nMoves):
        print("Brain with {} instructions".format(nMoves))
        self.instructions = []
        self.nMoves = nMoves


    def rndInstructions(self):
        for i in range(self.nMoves):
            self.instructions.append(vector.make2D(randint(0, 360)))
        for i in self.instructions:
            print(str(i.x) +";"+ str(i.y))

def main():
   tst = brain(100).rndInstructions()




if __name__ == "__main__":
    main()