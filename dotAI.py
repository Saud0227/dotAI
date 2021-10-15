from vectors import vector
from brain import brain


class dot():
    def __init__(self, bLength, sPos, gPos, isBest):
        self.pos = sPos
        
        self.g = gPos
        #Goal posistion, vector
        self.brain = brain(bLength)
        self.brain.rndInstructions()

        self.dotSpeed = 5
        self.isBest = isBest
        self.dead = False
        self.reachedGoal = False
        
        self.moveIndex = 0
        self.iscolided = False

    def __repr__(self):
        return f"<Dot object, Alive: {not self.dead}, id:{id(self)}>"
    def __str__(self):
        return f"<Dot: Alive:{not self.dead}, pos: {str(self.pos)}>"
    def update(self):
        if self.reachedGoal or self.isDead:
            pass
        elif self.moveIndex > self.brain.nMoves:
            self.move()
        else:
            self.isDead = True
    
    def move(self):
        cMove = self.brain.instruction[self.moveIndex]
        self.moveIndex+=1
        cMove.mult(self.dotSpeed)
        self.pos.add(cMove)

    

        
        
def main():
   tst1 = dot(1000,vector(100,20),vector(0,0), False)
   print(tst1.pos)
   print(tst1.brain)
   # print(tst1.brain.instructions)
   print(tst1)



if __name__ == "__main__":
    main()
