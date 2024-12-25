import math
class Figure:
    sides_count = 0
    def __init__(self,color,sides,filled=True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if (r>=0 and r<=255) and (g>=0 and g <=255) and (b>=0 and b<=255):
            return True
        else:
            return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r, g, b]
        else:
            self.__color = [self.__color[0],self.__color[1],self.__color[2]]

    def __is_valid_sides(self,sides):
        _f=True
        for i in sides:
            if i!=int(i): _f=False
        if self.sides_count != len(sides): _f=False
        return _f

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return  sum(self.__sides)

    def set_sides(self,*new_sides):
        if self.__is_valid_sides(new_sides):# -проверка на правильность данных для сторон
            if self.sides_count ==len(new_sides):#-проверка на количество данных для сторон
                self.__sides=[]
                for i in range(0,len(new_sides)):
                    self.__sides.append(new_sides[i])

class Circle(Figure):# меняем alon на args
    sides_count = 1
    def __init__(self,color,alon,*args):
        super().__init__(color,alon)
        self.set_sides(alon)
        if args == 0:
            self.__radius = 1
        else:
            self.__radius = alon/(2* math.pi)

    def get_square(self):
        return math.pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self,*sides):
        if len(sides) != 3:
            self.__a = 1
            self.__b = 1
            self.__c = 1
        else:
            self.__a = sides[0]
            self.__b = sides[1]
            self.__c = sides[2]
    def info_data(self):
        return self.__a,self.__b,self.__c
    def get_square(self):
        pp = (self.__a + self.__b + self.__c) /2
        return math.sqrt(pp*(pp-self.__a)*(pp-self.__b)*(pp-self.__c))

class Cube(Figure):
    sides_count = 12
    def __init__(self,color,*args):
        super().__init__(color,*args)
        gener_sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if len(args) == 1:
            gener_sides = []
            for i in range(0,self.sides_count):
                gener_sides.append(args[0])
        self.set_sides(*gener_sides)

    def get_volume(self):
        return self.__sides[0]**3


circle1 = Circle((200,200,100),10)
cube1 = Cube((222,35,130),6)
circle1.set_color(55,66,77)
print(circle1.get_color())

cube1.set_color(300,70,15)
print('цвет куба ',cube1.get_color())
# проверка на изменение сторон
cube1.set_sides(5,3,12,4,5) # не изменится
circle1.set_sides(15) # изменится
print(circle1.get_sides())
print('площадь круга ',circle1.get_square())
# проверка периметра(круга)
print(len(circle1))
# проверка объёма (куба):
#print(cube1.get_volume())

triangle1 = Triangle(10,20,25)
triangle1.set_color(5,4,2)                 # цвет 5,4,2
triangle1.set_color(5,4,500)               # цвет остался 5,4,2
print('цвет треугольника:',triangle1.get_color())
print('сторны треугольника:',triangle1.info_data())
print('площадь треугольника:',triangle1.get_square())
