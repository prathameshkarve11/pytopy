

class BankAccount:
    
    def __init__(self, accno, password, balance):
        self.accno = accno
        self.__password = password
        self.__balance = balance
        self.passcount = 0
        self.history =[]
        
    def deposit(self, amount, password):
        if self.passcount >= 3:
            print("account Locked!!")
            self.history.append("Attempted action but account locked")
            return 
     
        if password == self.__password:
            self.__balance += amount 
            self.passcount = 0
            self.history.append({
                "type": "deposit",
                "amount": amount,
                "status": "success"
            })
            print("Amount successfully deposited!")
        else:
            self.passcount +=1
            self.history.append(f" wrong pass entered at deposit ")
            print("Wrong password")


    def withdraw(self, amount, password):
        if self.passcount>= 3:
            print(" account locked!!")
            self.history.append("Attempted action but account locked")
            return 
       
        if password == self.__password:
            self.passcount = 0
            if amount <= self.__balance:
                self.__balance -= amount 
                self.history.append(f"ammount withdrawn : { amount} ")
                print("Amount withdrawn successfully")
            else:
                self.history.append(f" insufficient balance at withdrawal")
                print("Insufficient balance")
        else:
            self.passcount +=1
            self.history.append(f" wrong pass entered qat withdrawal")
            print("Wrong password")

    
    def get_balance(self, password):
        if self.passcount >= 3:
            print("account loacked")
            self.history.append("Attempted action but account locked")
            return 
        
        if password == self.__password:
            self.passcount = 0
            self.history.append(f"checked balance")
            return self.__balance
           
        else:
            self.passcount +=1
            self.history.append(f" wrong pass entered atttempt  get checking balance ")
            return "Wrong password"



ac1 = BankAccount(2334,"Prathu@123",240000)
# ac1.withdraw(500, "Prathu@123")
# ac1.get_balance("Prathu@123")
# ac1.withdraw(10000,  "Prathu@123")
# ac1.get_balance("Prathu@1234")
# ac1.get_balance("Prathu@12346")
# ac1.get_balance("Prathu66@1234")
# ac1.get_balance("Prathu@123")
# ac1.withdraw(500 ,"Prathu@123")
# print(ac1.history)

ac2 = BankAccount(3434,"Kavi@123", 1000)
ac2.deposit(500, "Kavi@123")
ac2.withdraw(7000 , "Kavi@123")
print(ac2.get_balance("Kavi@123"))
print(ac2.passcount)

ac2.get_balance("Kavi@12346")
ac2.get_balance("Kavi@12346")
ac2.get_balance("Kavi@12346")
ac2.get_balance("Kavi@12346")
ac2.deposit(400,"Kavi@123")
print(ac2.passcount)
ac2.deposit(400,"Kavi@123")
ac2.deposit(400,"Kavi@123")
print(ac2.history)
