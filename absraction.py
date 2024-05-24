class Account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc

    # Debit Method
  def debit(self,amount):
    self.balance -= amount
    print("Rs.", amount,"Was Debit")
   

   def credit(self,amount):
    
    self.balance -= amount
    print("Rs.", amount,"Was creidt")
   
