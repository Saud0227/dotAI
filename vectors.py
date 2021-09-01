import math as m

def pRound(n, decimals=0):
    multiplier = 10 ** decimals
    return m.floor(n*multiplier + 0.5) / multiplier


class vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mag(self):
        return pRound(m.sqrt(self.x*self.x + self.y*self.y),2)

    def normalize(self):
        tmpMag = self.mag()
        self.x = self.x/tmpMag
        self.y = self.y/tmpMag
        print(self.x,self.y,self.mag())
    
    def deg(self):
        cMag = self.mag()*-1
        topSideEq = cMag**2 + cMag**2 - ((cMag-self.y)**2 + self.x**2)
        bottomSideEq = 2 * cMag**2
        deg = m.degrees(m.acos(topSideEq/bottomSideEq))
        if(self.x<0):
            deg = 360-deg
        print(pRound(deg,2))
    
    def human(self):
        return("x:{}\nY:{}\nMag:{}".format(self.x,self.y,self.mag()))

def main():
    tmpV = vector(4,4)
    print(tmpV.human())
    tmpV.normalize()
    tmpV.deg()

if __name__ == "__main__":
    main()