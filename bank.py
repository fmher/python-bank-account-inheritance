
class BankAccount:

  def __init__(self, balance=0, interest_rate=0.02 ):
    self.balance = balance
    self.interest_rate = interest_rate

  def deposit(self, value):
    self.balance += value
    return self.balance
    


  def withdraw(self, value):
    if (self.balance >= 0):
      self.balance -= value
    else:
      print('Can not withdraw any negative amount.')
      return False


  def accumulate_interest(self):
    self.balance += self.balance * self.interest_rate
    return self.balance


class ChildrensAccount(BankAccount):
  def __init__(self):
    # invokes parents constructor, so if their balance 0, child balance will be 0
    super().__init__()
    self.interest_rate = 0

  def accumulate_interest(self):
    self.balance += 10
    return self.balance

  pass


class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40

  def withdraw(self, amount):
    #  test to see account will go negative
    negative_test = self.balance - amount
    # if acc will go negative, deduct the penalty adn return false
    if negative_test < 0:
      self.balance -= self.overdraft_penalty
      return False
    else:
      #  refer to the parents withdraw method
      #  otherwise, let them withdraw
      return super().withdraw(amount)

  def accumulate_interest(self):
    # only give interse if acc in good standing
    if self.balance < 0:
      return False
    else:
      return super().accumulate_interest()

  pass



# try:
#   basic_account = BankAccount()
#   basic_account.deposit(600)
#   print("Basic account has ${}".format(basic_account.balance))
#   basic_account.withdraw(17)
#   print("Basic account has ${}".format(basic_account.balance))
#   basic_account.accumulate_interest()
#   print("Basic account has ${}".format(basic_account.balance))
#   print()
# except Exception as e:
#   print(e)

# try:
#   childs_account = ChildrensAccount()
#   childs_account.deposit(34)
#   print("Child's account has ${}".format(childs_account.balance))
#   childs_account.withdraw(17)
#   print("Child's account has ${}".format(childs_account.balance))
#   childs_account.accumulate_interest()
#   print("Child's account has ${}".format(childs_account.balance))
#   print()
# except Exception as e:
#   print(e)
  

try:
  overdraft_account = OverdraftAccount()
  overdraft_account.deposit(12)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.withdraw(17)
  print("Overdraft account has ${}".format(overdraft_account.balance))
  overdraft_account.accumulate_interest()
  print("Overdraft account has ${}".format(overdraft_account.balance))
except Exception as e:
  print(e)
