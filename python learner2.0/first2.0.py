### python ooops cosepts 

class Car:
    tyre = True
    color = True
    wheels = 4


class lamborghini(Car):
    tyre = False
    __color = "red"
    speed = 34344

    def getcolor(self):
        print(self.__color)
    

class aventedor(lamborghini):
    __speed = 454545
    tyre = True
    color = "blue"

    def getspeed(self):
        print(self.__speed)
    
    def setspeed(self ,spe):
        self.__speed = spe
        

c1 = Car()
c2 = lamborghini()
c3 = aventedor()

print(c2.color)
c2.getcolor()
c3.getspeed()
c3.setspeed(909090)
c3.getspeed()
