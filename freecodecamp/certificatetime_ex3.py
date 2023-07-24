class Category:
    def __init__(self, name):
        self.name = name
        self.summ = 0
        self.ledger = []
        self.temp = dict()

    def deposit(self, money, descreption=''):
        temp = {"amount": money, "descreption": descreption}
        self.summ += money
        self.ledger.append(temp)

    def withdraw(self, money, descreption=''):
        money = '{:.2f}'.format(money)
        money = float(money)
        if (self.check_funds(money) == False):
            return False
        else:
            self.summ -= money
            temp = {"amount": -money, "descreption": descreption}
            self.ledger.append(temp)
            return True

    def get_balance(self):
        print('{:.2f}'.format(self.summ))


    def transfer(self, money, goto):
        to = 'Transfer to ' + str(goto.name)
        if(self.withdraw(money, to) == True):
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
        actual = ''
        othoni = ('{:*^30}\n'.format(self.name))
        actual += othoni
        for i in range(len(self.ledger)):
            desc = '{:<23}'.format(self.ledger[i]['descreption'][:23])
            amoun = '{:>7.2f}'.format(self.ledger[i]['amount'])
            actual += '{}{}\n'.format(desc,amoun)
        actual += 'Total: {:.2f}\n'.format(self.summ)
    


test = Category('Food')
test2 = Category('Entertainment')
test3 = Category('Business')

test.deposit(900, "deposit")
test2.deposit(900, "deposit")
test3.deposit(900, "deposit")

test.withdraw(45.67,'milk, cereal, eggs, bacon, bread')
test2.withdraw(33.40)
test3.withdraw(10.99)
test.transfer(20,test2)
test2.get_balance()

def create_spend_chart(categories):
    lista = []
    listaname = []
    summ = 0
    for i in range(len(categories)):
        lista.append(categories[i].name)
        for j in range(len(categories[i].ledger)):
            if(categories[i].ledger[j]['amount'] < 0):  
                lista.append(categories[i].ledger[j]['amount'])
                summ += categories[i].ledger[j]['amount']
    summ = abs(summ)
    print(lista)
    for i in range(len(lista)):
        try:
            if(lista[i].isalpha() == True):
                listaname.append(lista[i])
        except:
            temp = int((abs(lista[i])*100)/summ)
            if(temp >= 100):
                lista[i] = int((temp // 10*10)/10)
            else:
                lista[i] = int((temp // 10*10)/10)
    arithmoi = [i for i in range(0,110,10)]
    listanum = []
    temp = 0
    for i in range(0,len(lista)-1):
        if(type(lista[i]) == str and type(lista[i+1]) == str):
            listanum.append(0)
            temp = 0
            if(i == len(lista) - 2):
                listanum.append(0)
        if(type(lista[i]) == int and type(lista[i+1]) == int):
            temp = temp + lista[i+1]
            if(i == len(lista) - 2):
                listanum.append(temp)
        if(type(lista[i]) == int and type(lista[i+1]) == str):
            listanum.append(temp)
            temp = 0
            if(i == len(lista) - 2):
                listanum.append(0)
        if(type(lista[i]) == str and type(lista[i+1]) == int):
            temp += lista[i+1]
            if(i == len(lista) - 2):
                listanum.append(temp)
    print(lista)  
    print('Percentage spent by category')
    for i in range(len(arithmoi)):
        grammi = ''
        for j in range(len(listanum)):
            try:
                if(listanum[j].isalpha() == True):
                    continue
            except:
                if(listanum[j] * 10 >= arithmoi[-1-i]):
                    grammi += 'o  '
                else:
                    grammi += '   '
        print('{:>3}| {}'.format(arithmoi[len(arithmoi)-1-i],grammi))
    print('    {}'.format('-'*(len(listaname)*3+1)))
    l = 0
    while(l < (len(max(listaname,key=len)))):
        grammi = ''
        for i in range(len(listaname)):
            try:
                grammi += '{}  '.format(listaname[i][l])
            except:
                grammi += '   '
        print('    ',grammi)
        l += 1
    
            

create_spend_chart([test3,test,test2])
