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

    def update(self):
        if False:
            pass
        elif self.moveIndex > self.brain.nMoves and self.isDead == False:
            self.move()
        else:
            self.isDead = True
    
    def move(self):
        cMove = self.brain.instruction[self.moveIndex]
        self.moveIndex+=1
        cMove.mult(self.dotSpeed)

    

        
        
def main():
   tst1 = dot(1000,vector(100,20),vector(0,0), False)
   print(tst1.pos)
   print(tst1.brain)
   print(tst1.brain.instructions)



if __name__ == "__main__":
    main()
