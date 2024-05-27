class Faulty:
  def putdata(self):
    self.id= int(input('Enter your ID'))
    self.name = input('Enter your Name')
    self.salary = int(input('Enter your Faulty salary'))
    
  def display(self):
    print("Faulty ID", self.id)
    print("Enter you name", self.name)
    print("Enter your Faulty Salary", self.salary)
    
a = Faulty()
a.putdata()
a.display()
  
    