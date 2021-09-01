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
        cMag = self.mag() * -1
        dist = 

def main():
    tmpV = vector(10,-20)
    print(tmpV.human())
    tmpV.normalise()

if __name__ == "__main__":
    main()