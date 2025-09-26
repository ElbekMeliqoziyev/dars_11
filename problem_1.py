"""Rectangle klassini yozing.(10 ball)
1. Unda width, height property bo‘lsin.
2. area, perimeter metodlari qo‘shilsin.
3. Getter, setter, deleter ishlasin. """

# qayta ko'rib chiqish zarur
class Rectangle:
    def __init__(self,  width, height):
        self.__width = width
        self.__height = height

    @property
    def get_olcham(self):
        return self.__height, self.__width
    
    @get_olcham.setter
    def get_olcam(self, new, keng):
        self.__height = new
        self.__width = keng

    def area(self):
        return self.__height*self.__width
    
    def perimeter(self):
        return 2*(self.__height + self.__width)
    
r1 = Rectangle(2,3)

print(r1.get_olcham())
    

    

     