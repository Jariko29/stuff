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
            for i in range(self.width):
                if(kouti.width + i < self.width):
                    tempw += 1
            for i in range(self.height):
                if(kouti.height + i < self.height):
                    temph += 1      
            return tempw * temph

class Square(Rectangle):
    def __init__(self,plevra) -> None:
        self.side = plevra
        Rectangle.__init__(self,w=plevra,h=plevra)
        
    def __str__(self) -> str:
        protasi = f'Square(side={self.side})'
        return protasi
    
    def set_side(self,num) -> None:
        self.side = num
        Rectangle.set_height(num)
        Rectangle.set_width(num)

test = Rectangle(3,4)
print(test.get_diagonal())
print(test.get_picture())
print(test)
test2 = Square(3)
print(test2.get_area())
print(test2.get_picture())
print(test2)
