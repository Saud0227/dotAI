from vectors import vector



class dot():
    def __init__(self, sPos, gPos, isBest):
        self.pos = sPos
        
        self.g = gPos
        #Goal posistion, vector


        self.isBest = isBest
        self.dead = False
        self. reachedGoal = False
        
        
def main():
   tst1 = dot(vector(100,20),vector(0,0), False)
   print(tst1.pos)



if __name__ == "__main__":
    main()
