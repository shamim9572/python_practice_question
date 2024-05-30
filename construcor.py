class DemoClass:
  a = 10
  def __init__(self):
    print("Hi This Khan")
    
  def showvalue(self):
    self.c = self.a*self.a
    print(self.c)
    
  def showdata(self,a,b):
    print(a+b)
    
obj = DemoClass()
obj.showvalue()
obj.showdata(5,7)