import math as m

def pRound(n, decimals=0):
    multiplier = 10 ** decimals
    return m.floor(n*multiplier + 0.5) / multiplier


class vector():

    @staticmethod
    def degWrapping(deg):
         
        if(deg<0):
            return(360-deg)
        elif(deg>360):
            return(deg-360)
        else:
            return(deg)
    
    @classmethod
    def make2D(cls, deg):
        deg = cls.degWrapping(deg)
        invdeg = m.radians(cls.degWrapping(180-deg))
        #print(m.degrees(invdeg),cls.degWrapping(180-deg))
        tmpX = pRound(m.sin(invdeg),2)
        if(deg>180):
            tmpX*=-1
        tmpY = pRound(m.cos(invdeg),2)
        print(str(tmpX) + ";" + str(tmpY))
        


    

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
    """
    tmpV = vector(4,4)
    print(tmpV.human())
    tmpV.normalize()
    tmpV.deg()
    """
    for i in range(12):
        #print(360/12*i)
        vector.make2D(360/12*i)
if __name__ == "__main__":
    main()