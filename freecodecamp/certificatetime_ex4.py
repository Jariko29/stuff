class Rectangle(object):
    def __init__(self,w,h) -> None:
        self.width = w
        self.height = h
    
    def __str__(self) -> str:
        protasi = f'Rectangle(width={self.width}, height={self.height})'
        return protasi
    
    def set_width(self,num) -> None:
        self.width = num
        
    def set_height(self,num) -> None:
        self.height = num
        
    def get_area(self) -> int:
        return (self.height * self.width)
        
    def get_perimeter(self) -> int:
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self) -> float:
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self) -> str:
        if(self.width > 50 or self.height > 50):
            return 'Too big for picture.'
        else:
            shape = ''
            for i in range(self.height):
                shape += '*' * self.width + '\n'
            return shape

    def get_amount_inside(self,kouti) -> int:
        tempw = 0
        temph = 0
        if(kouti.width > self.width or kouti.height > self.height):
            return tempw
        else:
            for i in range(0,self.width,kouti.width):
                if(kouti.width + i <= self.width):
                    tempw += 1
                else:
                    break
            for i in range(0,self.height,kouti.height):
                if(kouti.height + i <= self.height):
                    temph += 1      
                else:
                    break
            return tempw * temph

class Square(Rectangle):
    def __init__(self,plevra) -> None:
        Rectangle.__init__(self,plevra,plevra)
        self.side = plevra
        
    def __str__(self) -> str:
        protasi = f'Square(side={self.side})'
        return protasi
    
    def set_side(self,n) -> None:
        self.side = n
        Rectangle.set_width(self,n)
        Rectangle.set_height(self,n)
    
    def set_width(self,n) -> None:
        self.set_side(n)
        Rectangle.set_width(self,n)
    
    def set_height(self,n) -> None:
        self.set_side(n)
        Rectangle.set_height(self,n)
        
    

test = Rectangle(15,10)
test2 = Square(4)
print(test2)
test2.set_height(5)
print(test2)
print(test.get_amount_inside(test2))