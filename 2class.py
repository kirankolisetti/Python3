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

cal1=Calculator(3,3);
print(cal1.Add());
print(cal1.REminder(2));
