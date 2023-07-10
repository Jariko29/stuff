class Category:
    def __init__(self,name):
        self.name = name
        self.summ = 0
        self.ledger = []
        self.temp = dict()
        
    def deposit(self,money,descreption=''):
        temp = {"amount":money,"description":descreption}
        self.summ += money
        self.ledger.append(temp)
        
    def print_elements(self):
        for i in range(len(self.ledger)):
            print('{:.2f} {}'.format(self.ledger[i]['amount'],self.ledger[i]['description']))
            
    def withdraw(self,money,descreption=''):
        if(self.check_funds(money) == 'False'): 
            return  'False'
        else:
            self.summ -= money
            temp = {"amount":-money,"description":descreption}
            self.ledger.append(temp)
            return 'True'
        
    def get_balance(self):
        print('{:.2f}'.format(self.summ))
        
    def transfer(self,money):
        print('g')
        
    def check_funds(self,money):
        if(self.summ < money):
            return 'Fasle'
        else:
            return 'True'
        
    
    
test = Category('Food')
test2 = Category('Clothes')
test3 = Category('Errands')

test.deposit(100,'initial deposit')
test2.deposit(18.21,'initial deposit')
test.withdraw(119.20,'Patixa')
test.print_elements()
test2.print_elements()
test.get_balance()


def create_spend_chart(categories): 
    print('g')