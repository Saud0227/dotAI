from vectors import vector
from dotAI import dot

class sim():
    def __init__(self, popS, bSize, grSize, sPos, gPos, blockers = None):
        self.gSize = grSize
        self.sPos = sPos
        self.gPos = gPos
        if blockers != None:
            self.blockers = blockers
        
        self.dots = []
        for i in range(popS):
            self.dots.append(dot(bSize, self.sPos, self.gPos,False))
        """ for i in self.dots:
            print(i.pos) """

    def checkBlockers(self,dotI):
        return true


    def mainTick(self):
        for d in self.dots:
            d.iscolided = self.checkBlockers(d)
            d.update()





def main():
    tst1 = sim(100, 1000,vector(200,600),vector(100,550),vector(100,10))
    print(tst1.dots)



if __name__ == '__main__':
    main()