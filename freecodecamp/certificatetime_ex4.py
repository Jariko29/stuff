import random
import copy
random.seed(95)
class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
    def draw(self,posa):
        if(posa < len(self.contents)):
            temp = []
            for i in range(posa):
                x = len(self.contents) * random.random()
                temp.append(self.contents[int(x)])
                self.contents.pop(int(x))
            return temp
        else:
            return False

hat1 = Hat(blue=3,red=2,green=6)
#hat2 = Hat(red=5, orange=4)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    hat = copy.copy(hat.contents)
    lista = []
    for k,v in expected_balls.items():
        for i in range(v):
            lista.append(k)
            
    prob = 0.0
    if(num_balls_drawn > len(hat)):
        prob = 1.0
        return prob
    for i in range(num_experiments):
        temp = []
        listatemp = []
        for c in range(len(hat)):
            listatemp.append(hat[c])
            
        for j in range(num_balls_drawn):
            y = random.randint(0,len(listatemp)-1)
            temp.append(listatemp[y])
            listatemp.pop(y)
        arxiko = len(temp)    
        for l in range(len(lista)):
            for o in range(len(temp)):
                if(lista[l] == temp[o]):
                    temp.pop(o)
                    break
        if(arxiko - len(lista) == len(temp)):
            prob += 1
    prob = float(prob / num_experiments)
    return prob
    
print(experiment(hat1, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))