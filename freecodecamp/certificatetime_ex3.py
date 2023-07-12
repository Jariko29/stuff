class Category:
    def __init__(self, name):
        self.name = name
        self.summ = 0
        self.ledger = []
        self.temp = dict()

    def deposit(self, money, descreption=''):
        temp = {"amount": money, "description": descreption}
        self.summ += money
        self.ledger.append(temp)

    def withdraw(self, money, descreption=''):
        money = '{:.2f}'.format(money)
        money = float(money)
        if (self.check_funds(money) == False):
            return False
        else:
            self.summ -= money
            temp = {"amount": -money, "description": descreption}
            self.ledger.append(temp)
            return True

    def get_balance(self):
        print('{:.2f}'.format(self.summ))

    def transfer(self, money, goto):
        to = 'Transfer to ' + str(goto.name)
        if (self.withdraw(money, to) == True):
            fromm = 'Transfer from ' + str(self.name)
            goto.deposit(money, fromm)
            return True
        else:
            return False

    def check_funds(self, money):
        if (self.summ < money):
            return False
        else:
            return True

    def __del__(self):
        telies = '*' * int((30/2-len(str(self.name))/2))
        othoni = ('{0}{1}{2}'.format(telies, self.name, telies))
        if (len(othoni) < 30):
            othoni = '*' + othoni
        print(othoni, '\a')
        for i in range(len(self.ledger)):
            print('{:<23}{:>7}'.format(
                self.ledger[i]['description'], self.ledger[i]['amount']))
        print('Total: {:.2f}'.format(self.summ))


test = Category('Food')
test2 = Category('Clothes')
test3 = Category('Errands')

test.deposit(100, 'initial deposit')
test2.deposit(18.21, 'initial deposit')
test3.deposit(50, 'initial deposit')
test.withdraw(19.20, 'Patixa')
test3.withdraw(25, 'revma')
test.transfer(50, test2)
test.get_balance()
test2.get_balance()


def create_spend_chart(categories):
    lista = []
    summ = 0
    count = 0
    for i in range(len(categories)):
        lista.append(categories[i].name)
        for j in range(len(categories[i].ledger)):
            if(categories[i].ledger[j]['amount'] < 0):  
                lista.append(categories[i].ledger[j]['amount'])
                summ += categories[i].ledger[j]['amount']
    summ = abs(summ)
    print(lista,summ)
    for i in range(len(lista)):
        try:
            if(lista[i].isalpha() == True):
                count += 1
                continue
        except:
            temp = int((abs(lista[i])*100)/summ)
            if(temp >= 100):
                lista[i] = int((temp // 10*10)/10)
            else:
                lista[i] = int((temp // 10*10)/10 + 1)
    arithmoi = [i for i in range(0,110,10)]
    print(count)
    print('Percentage spent by category')
    for i in range(len(arithmoi)):
        keno = '  '
        kiklos = ' '
        for i in range(count)
            if(lista[count]):
        print('{:>3}| {}  '.format(arithmoi[len(arithmoi)-1-i],kiklos))
    print(lista)
    
    
            

create_spend_chart([test,test2,test3])
