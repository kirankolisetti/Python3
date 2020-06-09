class Calculator(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def Add(self):
        return self.x+self.y;
    
    def Multi(self):
        return self.x*self.y;
    
    def REminder(self,z):
        self.z=z
        return (self.x*self.y)%self.z;


class Sical(Calculator):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z;
    
    def Divide(self):
        return self.x/self.z;
    
    def REminder(self):
        return (self.x*self.y)%self.z;




cal1=Sical(10,5,3);
print(cal1.Add());
print(cal1.Divide());
print(cal1.REminder());
