import math as m


class vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mag(self):
        return(m.sqrt(self.x*self.x + self.y*self.y))
    def normalise(self):
        tmpMag = self.mag()
        self.x = self.x/tmpMag
        self.y = self.y/tmpMag
        print(self.x,self.y,self.mag())

def main():
    tmpV = vector(10,-20)
    print(tmpV.mag())
    tmpV.normalise()

if __name__ == "__main__":
    main()